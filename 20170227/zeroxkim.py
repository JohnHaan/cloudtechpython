import random

def main():
	#print "Hello World!"
	#Print("Hello World!1")
	#print("Hello World!2")
	#print(Hello World!3)
	#print "Hello World!4"
	
	#lines = 0
	#while lines < 50:
	#	print(lines)
	#	lines = lines + 1
	
	#name = input("what is your name?\n")
	#print("hello ", name)
	
	ans1="Go for it!"
	ans2="No way, Jose!"
	ans3="I'm not sure. Ask me again."
	ans4="Fear of the unknown is what imprisons us."
	ans5="It would be madness to do that!"
	ans6="Only you can save mankind!"
	ans7="Makes no diffence to me, do or don't - whatever."
	ans8="Yes, I think on balance that is the right choice."
	
	choice = random.randint(1,8)
	if choice == 1:
		answer = ans1
	elif choice == 2:
		answer = ans2
	elif choice == 3:
		answer = ans3
	elif choice == 4:
		answer = ans4
	elif choice == 5:
		answer = ans5
	elif choice == 6:
		answer = ans6
	elif choice == 7:
		answer = ans7
	else:
		answer = ans8
	
	print (answer)
	
	input("\n\n press enter")

if __name__ == '__main__':
	main()

