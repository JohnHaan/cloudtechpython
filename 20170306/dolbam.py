# -*- coding:utf-8 -*-

# print("hello world")

# def times_tables(num, time):
# 	n=1
# 	while n <= time:
# 		print(n,"X",num,"=", n*num)
# 		n=n+1
		
# def main():
# 	print('한글 테스트')
# 	times_tables(12,12)

# if __name__ == '__main__':
# 	main()
	
import random

computer_number = random.randint(1, 100)
def is_same(target, number):
	if target == number:
		result="win"
	elif target > number:
		result="low"
	else:
		result="high"
	return result
print("안녕 \n 난 1부터 100중 숫자 하나를 골랐어요")

guess=int(input("뭔지 쓰고 엔터 키를 누르세요"))

higher_or_lower = is_same(computer_number, guess)

while higher_or_lower != "win":
	if higher_or_lower == "low":
		guess = int(input("높다. 다시"))
	else:
		guess = int(input("낮다. 다시"))
		
	higher_or_lower = is_same(computer_number, guess)
input("정답\n\n\n 마치려면 엔터")