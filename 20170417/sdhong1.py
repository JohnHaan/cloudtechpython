# -*- coding:utf-8 -*-

# 상속 실습 1

class Infrasil(object):
    name = "인프라실"
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
        print("%s님은 %s이며, %d살이고 기술을 선도합니다." % (self.leader, self.gender, self.age))
 

c = Cloudtechteam("이창재", 8, "남자", 36)
c.what_to_do()

#print(a.__dict__)
#print(Infrasil.__dict__)

### 참조 ( 객체 인스턴스 -> 참조 클래스 -> 전역변수)