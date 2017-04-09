# -*- coding:utf-8 -*-

#문제 1. 특정 서버를 헬스체크하여 접속 실패 여부를 특정 파일에 저장하는 프로그램을 작성하시오.
#  - 조건 : target url, target protocol, 로그 파일을 설정하는 설정파일을 정의하시오.
#  - 설정파일의 위치는 : /etc/{nicname}.conf로 정의합니다.

import pyping

A = raw_input("whay is IP\n")


check=pyping.ping(A)

if check.ret_code == 0:
	print("Success")
else:
	print("Connection Failed")





#문제 2. 리스트형 A의 중복값을 제거한 값을 출력하는 프로그램을 작성하시오.
#  - A의 인덱스값(A[i])의 타입에 따라 구분하여 중복값을 제거한다.
#  - ex> A = [1,2,2,4,5,5,9] => [1,2,4,5,9]
#  - ex> A = [{'x': 2, 'y': 3}, {'x': 1, 'y': 4}, {'x': 2, 'y': 3}, {'x': 2, 'y': 3}, {'x': 10, 'y': 15}]
#        => [{'x': 2, 'y': 3}, {'x': 1, 'y': 4}, {'x': 10, 'y': 15}]
        
#  - 입력값 리스트
#    (1) [1,5,2,1,9,1,5,10]
#    (2) ['apple', 'banana', 'kiwi', 'banana', 'melon', 'apple']
#    (3) [{'x': 2, 'y': 3}, {'x': 1, 'y': 4}, {'x': 2, 'y': 3}, {'x': 2, 'y': 3}, {'x': 10, 'y': 15}]