#모듈을 import 하여 사용할 때와 스크립트 전체를 실행할 때를 구분
#run.py이라는 모듈을 import 하여 사용할 경우 __name__ 은 run.py
#"python3.5 run.py"와 같이 스크립트를 바로 실행할 때 __name__ 은 __main__ 

#test2.py
from test1lib import *

def calc() :
    i = add(10,20)
    print(i)
    i = substract(20,5)
    print(i)
    
if __name__ == '__main__':
    calc()

## 스크립트 실행시 if __name__ 조건은 참이 되므로 calc() 실행