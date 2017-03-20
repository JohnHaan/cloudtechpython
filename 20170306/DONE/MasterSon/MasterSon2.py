import random
import string

computer_number = random.randint(1,100)

def is_same(target,number):
	if target == number:
		result="Win"
	elif target > number:
		result="Low"
	else:
		result="High"
	return result

if __name__ == '__main__':
	counter = 1
	print("1 to 100")
	guess = int(input("guess number : "))
	
	higher_or_lower = is_same(computer_number, guess)
		
	while higher_or_lower != "Win":
		if higher_or_lower == "Low":
			guess = int(input("high, retry : "))
		else:
			guess = int(input("low, retry : "))
		counter+=1
		higher_or_lower = is_same(computer_number, guess)
		
	if(higher_or_lower == "Win"):
		print("your guess count %d",counter)
		
	input("end of game")