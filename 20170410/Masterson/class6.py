class MyClass(object):
    def __init__(self, value):
        self.value = value
        print("Class is = ", value)
    
    def __del__(self):
        print("Class is deleted!")

foo = MyClass(1)