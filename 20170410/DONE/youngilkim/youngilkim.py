# -*- coding:utf-8 -*-

class Car:
    def __init__(self, name,color,seater,size):
        self.name = name
        self.color = color
        self.seater = seater
        self.size = size
        print(self.name, self.color, self.seater,self.size)

taxi = Car("taxi","주황","4","소형")
truck = Car("truck","초록","2","중형") 
bus = Car("bus","파란","15","대형")

