# -*- coding:utf-8 -*-

from __future__ import print_function


def lock_check(func):
    def wrapper(self):
        if self.state == 'lock':
            raise Exception('instance is lock !!')
        return func(self)
    return wrapper


class Instance(object):
    def __init__(self, name, state):
        self.name = name
        self.state = state
        print('%s : Current state is %s' % (self.name, self.state))

    @lock_check
    def reboot(self):
        print('%s : reboot ok !!' % self.name)

    @lock_check
    def stop(self):
        print('%s : stop ok !!' % self.name)


if __name__ == '__main__':
    instance = Instance('daemon', 'ok')
    instance.reboot()
    instance.stop()
    
    instance2 = Instance('daemon2', 'lock')
    instance2.reboot()
    #instance2.stop()