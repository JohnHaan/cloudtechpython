# -*- coding:utf-8 -*-

class Car:
    def __init__(self, name, color, seats, size):
        self.name = name
        self.color = color
        self.seats = seats
        self.size = size
        print(self.name, self.color, self.seats, self.size)

taxi = Car("taxi", "Orange","4","Small")
truck = Car("Truck", "Green","2","Medium") 
bus = Car("Bus", "Blue","15","Large")
