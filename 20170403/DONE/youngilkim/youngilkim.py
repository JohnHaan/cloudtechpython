import sys
import pyping
from oslo_config import cfg
from oslo_log import log as olog
from oslo_log import helpers as olog_helpers

OPTS = [
	cfg.StrOpt("target", default='www.google.com', help="health check target"),
	cfg.BoolOpt("is_udp", default=False, help="True or False")
]

@olog_helpers.log_method_call
def health_check(target,is_udp):
	r = pyping.ping(target, udp=is_udp)
	return r

def register_options(cfg):
    cfg.register_opts(OPTS, "health")
    cfg.register_cli_opts(OPTS, "health")

def main():
    LOG = olog.getLogger(__name__)
    CONF = cfg.CONF
    register_options(CONF)
    olog.register_options(CONF)
    CONF(sys.argv[1:], default_config_files=['/etc/youngilkim.conf'])
    olog.setup(CONF, 'demo')

    h_res = health_check(CONF.health.target,CONF.health.is_udp)
	
    if h_res.ret_code == 0:
        LOG.info("Success - %s, %s, max-rtt : %s", h_res.destination, h_res.destination_ip,h_res.max_rtt)
    elif h_res.ret_code != 0:
        LOG.error("Failed! - %s, %s", h_res.destination, h_res.destination_ip)

if __name__ == '__main__':
    main()