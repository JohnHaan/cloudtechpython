import random
import string

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
	computer_number = 0
	maxvalue=0
	level = raw_input("choice game level(e or m or h):")
	
	while(level != "e" and level != "m" and level != "h"):	
		level = raw_input("rechoice game level(e or m or h):")
	
	if(level == "e"):
		maxvalue=10
	elif(level == "m"):
		maxvalue=20
	elif(level == "h"):
		maxvalue=100
	
	
	computer_number = random.randint(1,maxvalue)
	print("1 to %d",maxvalue)
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
