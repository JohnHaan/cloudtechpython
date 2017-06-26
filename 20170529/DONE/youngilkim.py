def check_lock(func):
    def wrapper(self):
        if self.locked == "locked":
            raise Exception("Instance Locked!")
        return func(self)
    return wrapper

class Instance(object):
    def __init__(self, name, locked):
        self.name = name
        self.locked = locked

    @check_lock
    def reboot(self):
        print("Rebooting instance %s" % self.name)

    @check_lock
    def stop(self):
        print("Stopping instance %s" % self.name)


if __name__ == '__main__':
    instance1 = Instance('instance1','unlock')
    instance2 = Instance('instance2','locked')

    instance1.reboot()
    instance1.stop()

    instance2.reboot()