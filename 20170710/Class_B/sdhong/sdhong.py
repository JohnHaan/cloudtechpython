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
    
    
    
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    
    아 미안합니다. A반 수업중인데 방해했네요..
    
    사랑합니다 고객님
    숙제 다 하셨나요?