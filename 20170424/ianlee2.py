class Bird(object):
    def __init__(self):
        pass
    
    def fly(self):
        raise NotImplementedError
        
class Eagle(Bird):
    def __init__(self):
        super(Eagle, self).__init__()
        pass
        
    def fly(self):
        print("flyflfyflfyflfy")
        
eagle = Eagle()
eagle.fly()