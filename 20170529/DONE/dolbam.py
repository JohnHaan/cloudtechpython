
def is_lock(func):
    def wrapper(self):
        if self.is_lock == 'True':
            raise Exception("Instance is Locked")
        return func(self)
    return wrapper

class Instance(object):
    def __init__(self, **kargs):
        self.name = kargs.get("name", None)
        self.is_lock = kargs.get("is_lock", False)
    
    @is_lock       
    def reboot(self):
        print("Reboot %s" % self.name)
        
    @is_lock
    def stop(self):
        print("Stop %s" % self.name)

if __name__=='__main__':
    instance1 = Instance(name='instance1', is_lock='False')    
    instance1.reboot()
    instance1.stop()

    instance2 = Instance(name='instance2', is_lock='True')
    instance2.reboot()
    instance2.stop()
