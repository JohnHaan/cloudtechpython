# -*- coding:utf-8 -*-
import random

value = random.randint(1, 100)
mynumber = 'mynumber.py' * value

def is_same(target, number):
	if target == number:
		result="Win"
	elif target > number:
		result="Low"
	else:
		result="High"
	return result

print("mynumber.를 x번 곱했습니다. 몇 번을 곱했는지 맞춰보세요.")

guess = int(input("뭔지 쓰고 엔터 키를 누르세요."))


higher_or_lower = is_same(value, guess)
counter = [1]
counter.append(1)

while higher_or_lower != "Win":
	if higher_or_lower == "Low":
		guess = int(input("그것보단 높습니다. 다시 생각해보세요."))
	else:
		guess = int(input("그것보단 낮습니다. 다시 생각해보세요."))
		
	higher_or_lower = is_same(value, guess)
	
input("정답!\n잘했어요. \n\n\n마치려면 엔터 키를 누르세요.")

