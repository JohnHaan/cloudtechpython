# -*- coding:utf-8 -*-

import random

def is_same(target, number):
	if target == number:
		result="Win"
	elif target > number:
		result = "Low"
	else:
		result= "High"
	return result

def get_price(stock, count):
	return stock * count
	
def to_digit(price):
	digit_price = ''
	sprice = str(price)
	print(sprice)
	while len(sprice) > 3:
		chunk = sprice[-3:]
		if digit_price == '':
			digit_price = chunk
		else:
			digit_price = chunk + ',' + digit_price
		sprice = sprice[:-3]
		if len(sprice) <= 3:
			digit_price = sprice + ',' + digit_price
	return digit_price

def validate_level(level):
	while level !="e" and level !="m" and level !="h":
		level = input("죄송하지만 다시 입력해 주세요. 쉬운 게임은 'e'를, 중간 단계는 'm'을, 어려운\n"
					"단계를 하고 싶으면 'h'를 눌러주세요.\ne/m/h/:")
	return level

def main():
	### 문제 1
	daum_price = get_price(1000000, 32)
	naver_price = get_price(374392, 100)
	price = daum_price + naver_price
	digit_price = to_digit(price)
	print('문제 1번 답: {}'.format(digit_price))

	# ### 문제 2
	# computer_number = random.randint(1, 100)
	# print("안녕\n 난 1부터 100 중 숫자 하나를 골랐어요.")
	
	# guess = int(input("뭔지 쓰고 엔터 키를 누르세요."))
	
	# higher_or_lower = is_same(computer_number, guess)
	
	# counter = 0
	# while higher_or_lower != "Win":
	# 	if higher_or_lower == "Low":
	# 		guess = int(input("그것보단 높습니다. 다시 생각해보세요."))
	# 	else:
	# 		guess = int(input("그것보단 낮습니다. 다시 생각해보세요."))
	# 	counter += 1
	# 	higher_or_lower = is_same(computer_number, guess)
	
	# print('정답! {} 번 만에 맞추셨네요.\n'.format(counter))
	# input("마치려면 엔터키를 누르세요.")
	
	### 문제 3
	level = input("난이도를 선택하세요. e:쉽게, m:중간, h:어렵게 \n")
	level = validate_level(level)
	
	if level == 'e':
		computer_number = random.randint(1, 10)
		print("안녕\n 난 1부터 10 중 숫자 하나를 골랐어요.")
	elif level == 'm':
		computer_number = random.randint(1, 20)
		print("안녕\n 난 1부터 20 중 숫자 하나를 골랐어요.")
	elif level == 'h':
		computer_number = random.randint(1, 100)
		print("안녕\n 난 1부터 100 중 숫자 하나를 골랐어요.")
		
	guess = int(input("뭔지 쓰고 엔터 키를 누르세요."))
	
	higher_or_lower = is_same(computer_number, guess)
	
	counter = 0
	while higher_or_lower != "Win":
		if higher_or_lower == "Low":
			guess = int(input("그것보단 높습니다. 다시 생각해보세요.\n"))
		else:
			guess = int(input("그것보단 낮습니다. 다시 생각해보세요.\n"))
		counter += 1
		higher_or_lower = is_same(computer_number, guess)
	
	print('정답! {} 번 만에 맞추셨네요.\n'.format(counter))
	input("마치려면 엔터키를 누르세요.")
	
	### 문제 4
	ng = 'netmarblegames'
	result = {}
	for i in ng:
		if not i in result:
			result[i] = 1
		else:
			result[i] += 1
	print('문제 4번 답: {}'.format(result))

if __name__ == '__main__':
	main()