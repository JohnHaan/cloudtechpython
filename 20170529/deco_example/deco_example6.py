#### admin user에게만 함수 허용하기

# -*- coding:utf-8 -*-

class Greet(object):
    current_user = None
    
    def set_name(self, name):
        if name == 'admin':
            self.current_user = name
        else:
            raise Exception("권한이 없네요")

    def get_greeting(self, name):
        if name == 'admin':
            print("Hello {}".format(self.current_user))

greet = Greet()
greet.set_name('admin')
greet.get_greeting('admin')