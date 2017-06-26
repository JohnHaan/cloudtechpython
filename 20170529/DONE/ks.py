from functools import wraps

class ComputeNode(object):

    def __init__(self, **kwargs):
        self.name = kwargs.get("name", None)
        self.is_lock = kwargs.get("is_lock", False)

    def check_lock(func):

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if self.is_lock:
                raise "The instance is locked!"
            func(self, *args, **kwargs)

        return wrapper

    @check_lock
    def reboot(self):
        print("reboot")

    @check_lock
    def stop(self):
        print("start")

if __name__ == '__main__':
    instance1 = ComputeNode(name="node1")
    instance1.reboot()
    instance1.stop()
    instance2 = ComputeNode(name="node2", is_lock=True)
    instance2.reboot()
