# -*- coding:utf-8 -*-

### super() 실습 3

class Animal(object):
    def __init__(self):
        print("Animal __init__()")

class Tiger(Animal):
    def __init__(self):
#        super(Tiger, self).__init__()
        print("Tiger __init__()")

class Lion(Animal):
    def __init__(self):
#        super(Lion, self).__init__()
        print("Lion __init__()")

class Liger(Tiger, Lion):
    def __init__(self):
        super(Liger, self).__init__()
        print("Liger __init__()")
        
l = Liger()
