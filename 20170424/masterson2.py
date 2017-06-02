'''
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
        print("I will find you and ")

eagle = Eagle()
eagle.fly()
'''

class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg
    
def say_nick(nickname):
    if nickname == 'db':
        raise MyError('wow')
    print(nickname)

if __name__ == '__main__':
    for i in ['zeroxkim','db']:
        try:
            say_nick(i)
        except MyError as e:
            print(e)
