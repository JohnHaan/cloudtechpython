class Car:
    def __init__(self, name,color,seat,size):
        self.name = name
        self.color = color
        self.seat = seat
        self.size = size
        print(self.name, self.color, self.seat,self.size)

taxi = Car("taxi","orange","4","compact")
truck = Car("truck","green","2","middle") 
bus = Car("bus","blue","15","full")

