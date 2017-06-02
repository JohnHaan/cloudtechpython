# -*- coding:utf-8 -*-


class InstanceIsLocked(Exception):
    def __str__(self):
        return "instance is locked."

def check_instance_lock(func):
    def wrapper(self):
        if self.is_lock:
            raise InstanceIsLocked()
        return func(self)
    return wrapper

class Instance(object):
    def __init__(self, name, is_lock):
        self.name = name
        self.is_lock = is_lock

    @check_instance_lock
    def stop(self):
        print("%s is stopping now." % self.name)

    @check_instance_lock
    def reboot(self):
        print("%s is rebooting now." % self.name)

if __name__ == '__main__':
    instance1, instance2 = Instance("sjtest-1", False), Instance("sjtest-2", True)
    instance1.stop()
    instance2.reboot()