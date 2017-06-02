#### admin user에게만 함수 허용하기

# -*- coding:utf-8 -*-

def is_admin(func):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("아 진짜 안된다니까 그러네..")
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



  def is_lock(func)
  
  class Instance(object):
    self.name = name
    self.is_lock = False
    
    def reboot():
        print()
        
    def stop():