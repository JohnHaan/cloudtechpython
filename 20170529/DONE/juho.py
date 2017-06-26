def is_lock(func):
    def wrapper(*args, **kwargs):
        if(args[1] == True):
            raise Exception("no")
            return

        return func(*args, **kwargs)
    return wrapper

class Instance(object):
    name = None
    lock = False

    @is_lock
    def reboot(self, loc):
        print('reboot!')

    @is_lock
    def stop(self, loc):
        print('stop!')

ins = Instance()
ins.name = 'son'

ins.lock = False
ins.reboot(ins.lock)
ins.lock = True
ins.stop(ins.lock)
