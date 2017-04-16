# -*- coding:utf-8 -*-

class Service:
    secret = "영구는 배꼽이 두 개다"    # 유용한 정보
    def sum(self, a, b):                # 더하기 서비스
        result = a + b
        print("%s + %s = %s입니다." % (a, b, result))
        
pey = Service()

print(pey.secret)
pey.sum(1,1)
#Service.sum(pey, 1, 1)