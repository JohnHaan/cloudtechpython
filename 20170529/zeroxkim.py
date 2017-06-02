# -*- coding:utf-8 -*-

def is_admin(func):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("권한이 없네요")
        return func(*args, **kwargs)
    return wrapper

class Greet(object):
    current_user = None
    
    @is_admin
    def set_name(self, username):
        self.current_user = username
    
    @is_admin
    def get_greeting(self, username):
        print("Hello {}".format(self.current_user))

greet = Greet()
greet.set_name(username='admin')
greet.get_greeting(username='admin')
