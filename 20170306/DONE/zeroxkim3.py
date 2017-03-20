# myNumber.py
# This game uses a home made function

import random

# Create the function is_same()
def is_same(target, number):
	if target == number:
		result="Win"
	elif target > number:
		result="Low"
	else:
		result="High"
	return result

# Start the game
print("Hello.\nChoice your play level. easy is 'e', midium is 'm', hard is 'h'")
level = input("Choice your play level. ")
level_num = 0

# Level choice
while level != "e" and level != "m" and level != "h":
	level = input("Sorry, choice your play level. easy is 'e', midium is 'm', hard is 'h' ")
	
if level == "e":
	computer_number = random.randint(1, 10)
	level_num = 10
elif level == "m":
	computer_number = random.randint(1, 20)
	level_num = 20
else:
	computer_number = random.randint(1, 100)
	level_num = 100

print("I have thought of a number between 1 and %d." % level_num)

# Collect the user's guess as an integer
guess = int(input("Can you guess it? "))

# Use our function
higher_or_lower = is_same(computer_number, guess)

# Run the game until the user is correct
while higher_or_lower != "Win":
	if higher_or_lower == "Low":
		guess = int(input("Sorry, you are too low. Try again. "))
	else:
		guess = int(input("Sorry, you are too high. Try again. "))
	
	higher_or_lower = is_same(computer_number, guess)
	
# End the game
input("Correct!\nWell Done\n\n\nPress ENTER to exit.")
