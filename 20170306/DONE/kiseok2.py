# -*- coding:utf-8 -*-

import random

def is_same(target, number):
	if target == number:
		result = "win"
	elif target > number:
		result = "high"
	else:
		result = "low"
	return result


def main():
	while True:
		level = input("chice level you try(e,m,h):")
		if level == 'e':
			level_max = 10
			break
		elif level == 'm':
			level_max = 20
			break
		else:
			level_max = 100
			break
		print("sorry choice again (easy is e, medium is m, high is h)")
	counter = 1
	computer_number = random.randint(1,level_max)
	print(computer_number)
	print("hello i do choice 1-100!")
	guess = int(input("guess: "))
	higher_or_lower = is_same(computer_number, guess)
	#
	while higher_or_lower != "win":
		if higher_or_lower == "low":
			guess = int(input("lower than you guess: "))
		else:
			guess = int(input("higher than you guess: "))
		higher_or_lower = is_same(computer_number, guess)
		counter += 1
	
	print("your guess count are: %d." % counter)
	input("correct! enter to exit")


if __name__ == '__main__':
	main()
