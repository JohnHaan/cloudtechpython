# _*_ coding:utf-8 _*_

class Service:
    def __init__(self, name):
        self._secret = "영구는 머리가 두 가닥이다."
        self.name = name
    def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s 입니다." % (self.name, a, b, result))


pey = Service("ianlee")
print(pey._secret)
pey.sum(1,1)