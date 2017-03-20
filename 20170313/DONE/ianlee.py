#-*- coding:utf-8 -*-

""" 문제 1. python 내장 라이브러리를 활용하여, 현재 시간을 출력하는 프로그램을 작성하시오.
표시형식 : 2017-03-13 12:00:00"""

import time

d=time.localtime()
s="%04d-%02d-%02d %02d:%02d:%02d" % (d.tm_year, d.tm_mon, d.tm_mday, d.tm_hour, d.tm_mon, d.tm_sec)
print(s)



#문제 2. 특정 서버를 icmp protocol을 사용하여 헬스체크하여 접속 가능 시 "Success", 불가능 시 "Connection Failed" 를 표시하는 프로그램을 작성하시오.
#  -  hint : pyping 라이브러리를 활용

import pyping
#import ipaddress

#"d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" % 

A = raw_input("IP는 머요\n")


check=pyping.ping(A)

if check.ret_code == 0:
	print("Success")
else:
	print("Connection Failed")


#문제 3. 아래의 주어진 자료형을 stock 별로 주식 수를 더한 자료형으로 변환하는 프로그램을 작성하시오.
#[{'stock': 'naver', 'amount': 400}, {'stock': 'daum', 'amount': 300}, {'stock': 'naver', 'amount': 750}]

#=> {'naver': 1150, 'daum': 300}



# [{'stock': 'naver', 'amount': 400}, {'stock': 'daum', 'amount': 300}, {'stock': 'naver', 'amount': 750}, {'stock': 'netmarble', 'amount': 340}, {'stock': 'daum', 'amount': 500}, {'stock': 'nexon', 'amount': 1000}, {'stock': 'daum', 'amount': 650}]

