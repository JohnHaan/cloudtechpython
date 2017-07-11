# -*- coding:utf-8 -*-

# 오버라이딩 실습

class Infrasil(object):
    def __init__(self, leader, members):
        self.leader = leader
        self.members = members
    def what_to_do(self):
        print("%s님은 인프라를 담당합니다." % self.leader)
    def count_members(self):
        print(self.members)
    
class Cloudtechteam(Infrasil):
    def __init__(self, leader, members):
        self.leader = leader
        self.members = members
    def what_to_do(self):
        print("%s님은 기술을 선도합니다." % self.leader)

c = Cloudtechteam("이창재", 8)
c.what_to_do()

### 참조 ( 객체 인스턴스 -> 참조 클래스(자식 클래스-> 부모 클래스) -> 전역변수)