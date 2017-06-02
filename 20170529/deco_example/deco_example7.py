#### admin user에게만 함수 허용하기

# -*- coding:utf-8 -*-

def is_admin(user_name):
    if user_name != 'admin':
        raise Exception("권한이 없다니까요")

class Greet(object):
    current_user = None
    
    def set_name(self, name):
        is_admin(name)
        self.current_user = name

    def get_greeting(self, name):
        is_admin(name)
        print("Hello {}".format(self.current_user))

greet = Greet()
greet.set_name('admin')
greet.get_greeting('sjhan')