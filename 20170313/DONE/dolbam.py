#-*- coding:utf-8 -*-

#문제 1. python 내장 라이브러리를 활용하여, 현재 시간을 출력하는 프로그램을 작성하시오.
# &nbsp;- 표시형식 : "2017-03-13 12:00:00"

import time
print(time.strftime('%Y-%m-%d %H:%M:%S'))



#문제 2. 특정 서버를 icmp protocol을 사용하여 헬스체크하여 접속 가능 시 "Success", 불가능 시 "Connection Failed" 를 표시하는 프로그램을 작성하시오.
# &nbsp;- &nbsp;hint : pyping 라이브러리를 활용

import pyping


r = pyping.ping('google.com')


if r.ret_code == 0:
    print("Success")
else:
    print("Failed")



#문제 3. 아래의 주어진 자료형을 stock 별로 주식 수를 더한 자료형으로 변환하는 프로그램을 작성하시오.

dict1 = [{'stock': 'naver', 'amount': 400}, {'stock': 'daum', 'amount': 300}, {'stock': 'naver', 'amount': 750}]


res_dict = {}
for stock_dict in dict1:
        stock = stock_dict['stock']
        #naver daum naver
        amount = stock_dict['amount']
        #400 300 750
        
        if stock not in res_dict.keys():
            res_dict[stock] = amount
        else:
            res_dict[stock] += amount
print(res_dict)
    
    



