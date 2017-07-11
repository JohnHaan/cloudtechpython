#1. 호출
#from 모듈명 import 함수명
from math import factorial
n = factorial(5) / factorial(3)
print(n)

# 여러 함수를 import
from math import (factorial,acos)
n = factorial(3) + acos(1)
print(n)

# 모든 함수를 import
from math import *
n = sqrt(5) + fabs(-12.5) 
print(n)

# factorial() 함수를 f()로 사용 가능
from math import factorial as f
n = f(5) / f(3)
print(n)

#2. 호출 위치
#1.현재 디렉토리
#2. 환경변수 PYTHONPATH에 지정된 경로
#3. Python이 설치된 경로 및 그 밑의 라이브러리 경로

import sys
print(sys.path[0])
print(sys.path[1])
print(sys.path[2])
print(sys.path)

#sys.path.append('c:\pystudy')