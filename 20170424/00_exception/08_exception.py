# -*- coding:utf-8 -*-

# 다양한 예외 처리

def divide(a, b):
    return a / b
    
def main(a, b):
    try:
        c = divide(a, b)
    except ZeroDivisionError as e:
        print("두번째 인자는 0이어서는 안됩니다.(%s)" % e)
    except TypeError as e:
        print("모든 인자는 숫자여야 합니다.(%s)" % e)
    except:
        print("알 수 없는 에러가 발생했네요.")
    else:
        print("결과값 : %s" % c)
    finally:
        print("나누기 계산이 완료되었습니다.")
        
    
    
if __name__ == '__main__':
    main(5, 'string')