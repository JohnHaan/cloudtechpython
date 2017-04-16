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

a = Infrasil("강소륜", 30)
print(a.leader)
print(a.members)
a.what_to_do()
a.count_members()