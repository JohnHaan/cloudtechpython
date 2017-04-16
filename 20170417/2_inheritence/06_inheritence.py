# -*- coding:utf-8 -*-

### 다중상속 실습 1

class Tiger(object):
    def jump(self):
        print("호랑이처럼 멀리 점프하기")

class Lion(object):
    def bite(self):
        print("사자처럼 한입에 꿀꺽하기")

class Liger(Tiger, Lion):
    def play(self):
        print("라이거만의 사육사와 재미있게 놀기")
        
l = Liger()
l.bite()
l.jump()
l.play()