# -*- coding:utf-8 -*-

class Unit(object):
    def __init__(self, name, hp, movingspeed, strikingpower):
        self.name = name
        self.hp = hp
        self.movingspeed = movingspeed
        self.strikingpower = 5
        
    def attack(self):
        print("%s attacks enemy with %d strikingpower." % (self.name, self.strikingpower))
        
    def explain(self):
        print(self.__dict__)
        
class scv(Unit):
    def __init__(self, name, hp, movingspeed, strikingpower):
        super(scv, self).__init__(name, hp, movingspeed, strikingpower)
        self.strikingpower = strikingpower
        self.productivepower = 15
                
    def repair(self):
        print("%s repairs SiegeTank with %d productivepower." % (self.name, self.productivepower))
        
class marine(Unit):
    def __init__(self, name, hp, movingspeed, strikingpower):
        super(marine, self).__init__(name, hp, movingspeed, strikingpower)
        self.strikingpower = 10
        
    def patrol(self):
        print("%s patrols with %d movingspeed." % (self.name, self.movingspeed))
        
class vulture(Unit):
    def __init__(self, name, hp, movingspeed, strikingpower):
        super(vulture, self).__init__(name, hp, movingspeed, strikingpower)
        self.strikingpower = 25
        self.minecount = 3
        
def main():
    a = Unit("test unit", 1, 2, 3)
    a.attack()
    print("")
    
    b = scv("scv", 50, 10, 100)
    b.explain()
    b.repair()
    b.attack()
    print("")
    
    c = marine("marine", 100, 12, 100)
    c.explain()
    c.attack()
    c.patrol()
    print("")
    
    d = vulture("vulture", 150, 20, 100)
    d.explain()
    d.attack()

if __name__ == '__main__':
    main()
    