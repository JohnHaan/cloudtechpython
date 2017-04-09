# -*- coding:utf-8 -*-

### Class 이해하기 1
result = 0

def adder(num):
    global result
    result += num
    return result

print(adder(3))
print(adder(4))