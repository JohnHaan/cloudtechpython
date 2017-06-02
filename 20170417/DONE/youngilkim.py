# -*- coding:utf-8 -*-

class units(object):
    def __init__(self,name,hp,speed,power=5):
        self.name=name
        self.hp=hp
        self.speed=speed
        self.power=power
    def attack(self):
        print("%s attack : %s" % (self.name,self.power))
    def explain(self):
        print("explain %s : %s" % (self.name,self.__dict__))
        
class scv(units):
    def __init__(self,name,hp,speed,power,prod):
        super(scv, self).__init__(name,hp,speed,power)
        self.prod=prod
    def repair(self):
        print("repair %s" % self.name)
            
class marin(units):
    def __init__(self,name,hp,speed,power=10):
        super(marin, self).__init__(name,hp,speed,power)
    def patrol(self):
        print("patrol %s" % self.name)
    
class vulture(units):
    def __init__(self,name,hp,speed,power=25,minecnt=5):
        super(vulture, self).__init__(name,hp,speed,power)
        self.minecnt=minecnt

scv=scv("scv","50","5","5","5")
scv.explain()
scv.attack()
scv.repair()
marin=marin("marin","100","7","10")
marin.explain()
marin.attack()
marin.patrol()
vulture=vulture("vulture","120","10")
vulture.explain()
vulture.attack()