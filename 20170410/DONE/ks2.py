# https://github.com/openstack/neutron/blob/master/neutron/agent/linux/ip_lib.py#L70-L267

class SubProcessBase(object):
    def __init__(self, namespace=None,
                 log_fail_as_error=True):
        self.namespace = namespace
        self.log_fail_as_error = log_fail_as_error
        try:
            self.force_root = cfg.CONF.ip_lib_force_root
        except cfg.NoSuchOptError:
            # Only callers that need to force use of the root helper
            # need to register the option.
            self.force_root = False

    def _run(self, options, command, args):
        if self.namespace:
            return self._as_root(options, command, args)
        elif self.force_root:
            # Force use of the root helper to ensure that commands
            # will execute in dom0 when running under XenServer/XCP.
            return self._execute(options, command, args, run_as_root=True,
                                 log_fail_as_error=self.log_fail_as_error)
        else:
            return self._execute(options, command, args,
                                 log_fail_as_error=self.log_fail_as_error)

    def _as_root(self, options, command, args, use_root_namespace=False):
        namespace = self.namespace if not use_root_namespace else None

        return self._execute(options, command, args, run_as_root=True,
                             namespace=namespace,
                             log_fail_as_error=self.log_fail_as_error)

    @classmethod
    def _execute(cls, options, command, args, run_as_root=False,
                 namespace=None, log_fail_as_error=True):
        opt_list = ['-%s' % o for o in options]
        ip_cmd = add_namespace_to_cmd(['ip'], namespace)
        cmd = ip_cmd + opt_list + [command] + list(args)
        return utils.execute(cmd, run_as_root=run_as_root,
                             log_fail_as_error=log_fail_as_error)

    def set_log_fail_as_error(self, fail_with_error):
        self.log_fail_as_error = fail_with_error

    def get_log_fail_as_error(self):
        return self.log_fail_as_error


class IPWrapper(SubProcessBase):
    def __init__(self, namespace=None):
        super(IPWrapper, self).__init__(namespace=namespace)
        self.netns = IpNetnsCommand(self)

    def device(self, name):
        return IPDevice(name, namespace=self.namespace)

    def get_devices(self, exclude_loopback=False, exclude_gre_devices=False):
        retval = []
        if self.namespace:
            # we call out manually because in order to avoid screen scraping
            # iproute2 we use find to see what is in the sysfs directory, as
            # suggested by Stephen Hemminger (iproute2 dev).
            try:
                cmd = ['ip', 'netns', 'exec', self.namespace,
                       'find', SYS_NET_PATH, '-maxdepth', '1',
                       '-type', 'l', '-printf', '%f ']
                output = utils.execute(
                    cmd,
                    run_as_root=True,
                    log_fail_as_error=self.log_fail_as_error).split()
            except RuntimeError:
                # We could be racing with a cron job deleting namespaces.
                # Just return a empty list if the namespace is deleted.
                with excutils.save_and_reraise_exception() as ctx:
                    if not self.netns.exists(self.namespace):
                        ctx.reraise = False
                        return []
        else:
            output = (
                i for i in os.listdir(SYS_NET_PATH)
                if os.path.islink(os.path.join(SYS_NET_PATH, i))
            )

        for name in output:
            if (exclude_loopback and name == LOOPBACK_DEVNAME or
                    exclude_gre_devices and name in GRE_TUNNEL_DEVICE_NAMES):
                continue
            retval.append(IPDevice(name, namespace=self.namespace))

        return retval

    def get_device_by_ip(self, ip):
        """Get the IPDevice from system which has ip configured.
        @param ip: look for the device holding this ip. If this is None,
                   None is returned.
        @type ip: str.
        """
        if not ip:
            return None

        addr = IpAddrCommand(self)
        devices = addr.get_devices_with_ip(to=ip)
        if devices:
            return IPDevice(devices[0]['name'], namespace=self.namespace)

    def add_tuntap(self, name, mode='tap'):
        self._as_root([], 'tuntap', ('add', name, 'mode', mode))
        return IPDevice(name, namespace=self.namespace)

    def add_veth(self, name1, name2, namespace2=None):
        args = ['add', name1, 'type', 'veth', 'peer', 'name', name2]

        if namespace2 is None:
            namespace2 = self.namespace
        else:
            self.ensure_namespace(namespace2)
            args += ['netns', namespace2]

        self._as_root([], 'link', tuple(args))

        return (IPDevice(name1, namespace=self.namespace),
                IPDevice(name2, namespace=namespace2))

    def add_macvtap(self, name, src_dev, mode='bridge'):
        args = ['add', 'link', src_dev, 'name', name, 'type', 'macvtap',
                'mode', mode]
        self._as_root([], 'link', tuple(args))
        return IPDevice(name, namespace=self.namespace)

    def del_veth(self, name):
        """Delete a virtual interface between two namespaces."""
        self._as_root([], 'link', ('del', name))

    def add_dummy(self, name):
        """Create a Linux dummy interface with the given name."""
        self._as_root([], 'link', ('add', name, 'type', 'dummy'))
        return IPDevice(name, namespace=self.namespace)

    def ensure_namespace(self, name):
        if not self.netns.exists(name):
            ip = self.netns.add(name)
            lo = ip.device(LOOPBACK_DEVNAME)
            lo.link.set_up()
        else:
            ip = IPWrapper(namespace=name)
        return ip

    def namespace_is_empty(self):
        return not self.get_devices(exclude_loopback=True,
                                    exclude_gre_devices=True)

    def garbage_collect_namespace(self):
        """Conditionally destroy the namespace if it is empty."""
        if self.namespace and self.netns.exists(self.namespace):
            if self.namespace_is_empty():
                self.netns.delete(self.namespace)
                return True
        return False

    def add_device_to_namespace(self, device):
        if self.namespace:
            device.link.set_netns(self.namespace)

    def add_vlan(self, name, physical_interface, vlan_id):
        cmd = ['add', 'link', physical_interface, 'name', name,
               'type', 'vlan', 'id', vlan_id]
        self._as_root([], 'link', cmd)
        return IPDevice(name, namespace=self.namespace)

    def add_vxlan(self, name, vni, group=None, dev=None, ttl=None, tos=None,
                  local=None, port=None, proxy=False):
        cmd = ['add', name, 'type', 'vxlan', 'id', vni]
        if group:
            cmd.extend(['group', group])
        if dev:
            cmd.extend(['dev', dev])
        if ttl:
            cmd.extend(['ttl', ttl])
        if tos:
            cmd.extend(['tos', tos])
        if local:
            cmd.extend(['local', local])
        if proxy:
            cmd.append('proxy')
        # tuple: min,max
        if port and len(port) == 2:
            cmd.extend(['port', port[0], port[1]])
        elif port:
            raise n_exc.NetworkVxlanPortRangeError(vxlan_range=port)
        self._as_root([], 'link', cmd)
        return (IPDevice(name, namespace=self.namespace))

    @classmethod
    def get_namespaces(cls):
        output = cls._execute(
            [], 'netns', ('list',),
            run_as_root=cfg.CONF.AGENT.use_helper_for_ns_read)
        return [l.split()[0] for l in output.splitlines()]
