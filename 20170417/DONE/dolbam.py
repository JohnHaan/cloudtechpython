class Unit(object):
    def __init__(self, name, hp, speed, power=5):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.power = power
    
    def attack(self):
        print("\n%s Attack Power = %d" % (self.name, self.power))

class Scv(Unit):
    def __init__(self, name, hp, speed, power, prod):
        super(Scv,self).__init__(name, hp, speed, power)
        self.prod = prod
    def explain(self):
        print("\nNAME:%s, HP:%d, SPEED:%d, POWER:%d, PROD:%d" % (self.name, self.hp, self.speed, self.power, self.prod))
        
class Marine(Unit):
    def __init__(self, name, hp, speed, power=10):
        super(Marine, self).__init__(name, hp, speed, power)
    
    def explain(self):
        print("\nNAME:%s, HP:%d, SPEED:%d, POWER:%d" % (self.name, self.hp, self.speed, self.power))

class Vulture(Unit):
    def __init__(self, name, hp, speed, power, mine):
        super(Vulture, self).__init__(name, hp, speed, power)
        self.mine = mine

    def explain(self):
        print("\nNAME:%s, HP:%d, SPEED:%d, POWER:%d MINE:%d" % (self.name, self.hp, self.speed, self.power, self.mine))
    
scv = Scv('SCV', 10, 2, 5, 20)
scv.explain()
scv.attack()

marine = Marine('Marine', 12, 4)
marine.explain()
marine.attack()

vulture = Vulture('Vulture', 30, 25, 15, 3)
vulture.explain()
vulture.attack()