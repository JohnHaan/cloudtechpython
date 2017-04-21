# -*- coding:utf-8 -*-

# 상속 실습 1

#a.name = "Infra Dev"
#print(a.name)

class Infrasil(object):
    name = "인프라실"
    def __init__(self, leader, members):
        self.leader = leader
        self.members = members

a = Infrasil("강소륜", 30)
print(a.name)

a.name = "Infra Dev"
print(a.name)

#print(a.__dict__)
#print(Infrasil.__dict__)

### 참조 ( 객체 인스턴스 -> 참조 클래스 -> 전역변수)