
import random

def main():
	ans1="Go for it!"
	ans2="No way, Jose!"
	ans3="I'm not sure. Ask me again."
	ans4="Fear of the unknown is what imprisons us."
	ans5="It would be madness to do that!"
	ans6="Only you can save mankind!"
	ans7="Makes no diffence to me, do or don't - whatever."
	ans8="Yes, I think on balance that is the right choice."
	print("Welcome to My8Ball.")
	# get the users question
	question = input("Ask me for advice then press ENTER to shake me.\n")
	print("shaking ...\n" * 4)
	choise = random.randint(1,8)
	if choise == 1:
		answer = ans1
	elif choise == 2:
		answer = ans2
	elif choise == 3:
		answer = ans3
	elif choise == 4:
		answer = ans4
	elif choise == 5:
		answer = ans5
	elif choise == 6:
		answer = ans6
	elif choise == 7:
		answer = ans7
	else:
		answer = ans8	
	print(answer)


if __name__ == '__main__':
	main()
