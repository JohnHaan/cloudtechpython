# 두개의 입력파라미터를 받아들여 이를 더한 값을 리턴
def sum(a, b):
    s = a + b
    return s
 
total = sum(4, 7)
print(total)


# 디폴트 파라메터
def calc(i, j, factor = 1):
    return i * j * factor
 
result = calc(10, 20)
print(result)


# named parameter #어떤 값이 어떤 파라미터로 전달되는지 쉽게 파악
def report(name, age, score):
    print(name, score)
 
report(age=10, name="Kim", score=80)


#가변길이 파라메터 #0부터 N개의 파라미터를 받아들이도록

def total(*numbers):
    tot = 0
    for n in numbers:
        tot += n
    return tot
 
t = total(1,2)
print(t)

t = total(1,5,2,6)
print(t)

# decorator #함수위에 붙이면 함수보다 먼저 실행
def decorator_function(original_function):
    def wrapper_function():
      print('{} 함수가 호출되기전 입니다.'.format(original_function.__name__))
      return original_function()
    return wrapper_function

class decorator_test(object):
  def __init__(self,fff):
    print("생성자")
    fff()
    
  def __call__(self):
    print("호출됨")

@decorator_test  #1
def display_1():
    print ('display_1 함수가 실행됐습니다.')

@decorator_function  #2
def display_2():
    print ('display_2 함수가 실행됐습니다.')

# display_1 = decorator_function(display_1)  #3
# display_2 = decorator_function(display_2)  #4

display_1()
display_2()