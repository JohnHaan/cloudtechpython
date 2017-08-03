# 모듈이란 무엇인가?
# 모듈이란 함수나 변수, 클래스들을 모아놓은 파일이다.
# 모듈은 다은 파이썬 프로그램에서 불서 쓸 수 있다.

# mod1.py
def sum(a, b):
    return a + b
    
#모듈을 불러오려면?
#import 모듈이름 (모듈이름에 확장자는 쓰지 않는다!)

#도트연산자
#모듈파일의 함수를 이용하기 위해서는 파일이름.(도트연산자)함수이름 형태로 사용한다.
#mod1.sum

def safe_sum(a, b):
    if type(a) != type(b):
        print "더할수 있는 것이 아닙니다."
        return
    else:
        result = sum(a, b)
    return result
    
# a,b의 타입을 비교해서 다르면 더할 수 없다.


# 동일 모듈에 다른 모듈함수를 호출하는 경우  mod1.sum, mod1.safe_sum 이렇게 쓰면 불편하다. from 모듈이름 import 모듈함수를 사용하면 된다.
# 동일 모듈의 여러 모듈함수를 사용하고 싶으면 from 모듈이름 import 모듈함수1, 모듈함수2
# 동일 모듈의 모든 모듈함수를 사용하고 싶으면 from 모듈이름 import *


# if __name__ == "__main__": 의 의미

if __name__ == "__main__":
	print safe_sum('a', 1)
	print safe_sum(1, 4)
	print sum(10, 10.4)
	
	
	
	
# 모듈을 불러오기 위해서는 파이썬파일이 모듈과 동일 경로에 있어야한다.
# 경로에 상관없이 불러오기 위해서는 sys모듈을 이용하여 path를 지정한다.
>>> sys.path.append("C:\Python\Mymodules")
>>> sys.path
['', 'c:\\', 'c:\\python21\\dlls', 'c:\\python21\\lib', 'c:\\python21\\lib\\plat
-win', 'c:\\python21\\lib\\lib-tk', 'c:\\python21', 'C:\\Python\\Mymodules']
>>>