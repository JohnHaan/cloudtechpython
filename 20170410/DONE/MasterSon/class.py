class Car(object):
    def __init__(self, color, count, size):
        self.color = color
        self.count = count
        self.size = size

def main():
    taxi1 = Car('orange',4,'small')
    truck1 =Car('green',2,'medium')
    bus1 = Car('blue',15,'large')
    pass

if __name__ == '__main__':
    main()
