# -*- coding:utf-8 -*-

class Infrasil(object):
    name = "인프라실"
    def __init__(self, leader, members):
        self.leader = leader
        self.members = members
    
    def what_to_do(self):
        print("%s is infrasil" % self.leader)
        
    def count_members(self):
        print(self.members)
        
class Cloudtechteam(Infrasil):
    def __init__(self, leader, members, gender, age):
        super(Cloudtechteam, self).__init__(leader, members)
        self.gender = gender
        self.age = age
        
    def what_to_do(self):
        print("%s is %s, %s age and tech leader" % (self.leader, self.gender, self.age))
        
    def count_members(self):
        print("how many?")
        super().count_members()
a = Infrasil("강소륜", 30)
print(a.leader)
print(a.members)

a.what_to_do()
a.count_members()

c = Cloudtechteam("ianlee", 8, "man", 36)
print(c.leader)
print(c.members)

c.what_to_do()
c.count_members()
