
class MyClass(object):
    def __init__(self, value):
        self.value = value
        print("class is created val = ", value)

    def __del__(self):
        print("class is deleted")

foo = MyClass(1)
