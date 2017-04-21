class Animal(object):
    def __init__(self):
        print("animal.__init__()")

class Tiger(Animal):
    def __init__(self):
        super(Tiger,self).__init__()
        print("tiger.__init__()")
    def jump(self):
        print("jump like tiger")
    def cry(self):
        print("tiger cry")

class Lion(Animal):
    def __init__(self):
        super(Lion,self).__init__()
        print("lion.__init__()")
    def bite(self):
        print("bite like lion")
    def cry(self):
        print("lion cry")

class Liger(Tiger, Lion):
    def __init__(self):
        super(Liger,self).__init__()
    def play(self):
        print("play with man")

l = Liger()
#l.jump()
#l.bite()
#l.play()
#l.cry()
print(Liger.__mro__)
