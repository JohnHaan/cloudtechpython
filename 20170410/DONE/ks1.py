class Car(object):
    color = None
    seat = None
    size = None

class Taxi(Car):
    def __init__(self):
        self.color = "orange"
        self.seat = 4
        self.size = "small"

class Truck(Car):
    def __init__(self):
        self.color = "green"
        self.seat = 2
        self.size = "medium"

class Bus(Car):
    def __init__(self):
        self.color = "blue"
        self.seat = 15
        self.size = "large"

taxi = Taxi()
truck = Truck()
bus = Bus()

for o in [taxi, truck, bus]:
    print (o, o.color, o.seat, o.size)
