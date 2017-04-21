# -*- coding:utf-8 -*-

# 상속 실습 1

class Infrasil(object):
    def __init__(self, leader, members):
        self.leader = leader
        self.members = members
    def what_to_do(self):
        print("%s님은 인프라를 담당합니다." % self.leader)
    def count_members(self):
        print(self.members)

class Cloudtechteam(Infrasil):
    def __init__(self, leader, members, gender, age):
        super(Cloudtechteam, self).__init__(leader, members)
        self.gender = gender
        self.age = age
    def what_to_do(self):
        print("%s 님은 %s 이며, %s살이고 기술을 선도합니다." % (self.leader, self.gender, self.age))
    def count_members(self):
        print("몇명이지?")
        super().count_members()
        
c = Cloudtechteam("이창재", 8, "남자", 36)
print(c.leader)
print(c.members)
c.what_to_do()
c.count_members()
#a = Infrasil("강소륜", 30)
#print(a.leader)
#print(a.members)
#a.what_to_do()
#a.count_members()