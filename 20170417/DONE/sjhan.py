# -*- coding:utf-8 -*-

class Unit(object):
    def __init__(self, name, hp, speed, attack_power=5):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.attack_power = attack_power

    def attack(self):
        print("Attack! My Attack Power is %s" % self.attack_power)

class Scv(Unit):
    def __init__(self, name, hp, speed, attack_power, prd_power):
        super(Scv, self).__init__(name, hp, speed, attack_power)
        self.prd_power = prd_power
    def explain(self):
        print("SCV Attrs : %s" % self.__dict__)

class Marine(Unit):
    def __init__(self, name, hp, speed, attack_power=10):
        super(Marine, self).__init__(name, hp, speed, attack_power)
    
    def explain(self):
        print("Marine Attrs : %s" % self.__dict__)

class Vulture(Unit):
    def __init__(self, name, hp, speed, attack_power, num_mine):
        super(Vulture, self).__init__(name, hp, speed, attack_power)
        self.num_mine = num_mine

    def explain(self):
        print("Vulture Attrs : %s" % self.__dict__)

scv = Scv('scv', 60, 10, 5, 10)
scv.explain()
scv.attack()
marine = Marine('marine', 50, 10)
marine.explain()
marine.attack()
vulture = Vulture('vulture', 120, 30, 25, 3)
vulture.explain()
vulture.attack()