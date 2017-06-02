import sys

def devision(a,b):
    try:
        c=a/b
    except (ZeroDivisionError, TypeError) as e:
        print(e)
    except:
        print("에러가 발생하였습니다.")
    else:
        print("%d / %d = %d" % (a,b,c))
    finally:
        print("나눗셈 계산이 완료되었습니다.")
        

devision(10,5)
devision("a","b")
devision(10,0)