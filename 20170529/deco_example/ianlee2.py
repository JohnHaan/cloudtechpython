# _*_ coding:utf-8 _*_

def is_admin(func):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("아 진짜 안된다니깐 그러네..")
        return func(*args, **kwargs)
    return wrapper


class Greet(object):
    current_user = None
    
    @is_admin
    def set_name(self, name):
        self.current_user = name
        
    @is_admin
    def get_greeting(self, name):
        print("Hello {}".format(self.current_user))

greet = Greet()
greet.set_name('admin')
greet.get_greeting('ianlee')