# -*- coding:utf-8 -*-

## super 실습 3

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
        print("%s님은 %s이며, %s살이고 기술을 선도합니다." % (self.leader, self.gender, self.age))

b = Cloudtechteam("이창재", 8, "남자", 36)
b.what_to_do()
b.count_members()