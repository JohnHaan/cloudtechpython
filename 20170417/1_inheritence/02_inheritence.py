# -*- coding:utf-8 -*-


class Infrasil(object):
    def __init__(self, leader, members):
        self.leader = leader
        self.members = members
    def what_to_do(self):
        print("%s님은 인프라를 담당합니다." % self.leader)
    def count_members(self):
        print(self.members)

class Cloudtechteam(infrasil):
    def __init__(self, leader, members):
        self.leader = leader
        self.members = members

c = Cloudtechteam("이창재", 8)
print(c.leader)
print(c.members)
c.what_to_do()
c.count_members()
