class Car(object):
    pass
    
class Taxi(Car):
    def __init__(self):
        self.color = "orange"
        self.seat = 4
        self.size = "small"
        print(self, self.color, self.seat, self.size)

class Truck(Car):
    def __init__(self):
        self.color = "green"
        self.seat = 2
        self.size = "medium"
        print(self, self.color, self.seat, self.size)
        
class Bus(Car):
    def __init__(self):
        self.color = "blue"
        self.seat = 15
        self.size = "large"
        print(self, self.color, self.seat, self.size)
        
taxi = Taxi()
truck = Truck()
bus = Bus()

