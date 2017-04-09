# -*- coding:utf-8 -*-

class Service:
    def __init__(self, name):
        self._secret = "영구는 배꼽이 두 개다"
        self.name = name
    def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s입니다." % (self.name, a, b, result))
        

pey = Service("john haan")
print(pey._secret)
pey.sum(1,1)