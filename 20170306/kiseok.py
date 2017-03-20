# -*- coding:utf-8 -*-

import random

def is_same(target, number):
	if target == number:
		result = "win"
	elif target > number:
		result = "low"
	else:
		result = "high"
	return result


def main():
	computer_number = random.randint(1,100)
	print(computer_number)
	print("hello i do choice 1-100!")
	guess = int(input("guess: "))
	higher_or_lower = is_same(computer_number, guess)
	#
	while higher_or_lower != "win":
		if higher_or_lower == "low":
			guess = int(input("lower than you guess: "))
		else:
			quess = int(input("higher than you guess: "))
		higher_or_lower = is_same(computer_number, guess)
	
	input("correct! enter to exit")


if __name__ == '__main__':
	main()
