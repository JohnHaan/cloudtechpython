import random

ans1="ja"
ans2="ok"
ans3="what?"
ans4="don't know"
ans5="7p?"
ans6="you"
ans7="he"
ans8="ok"
def main():
	choice=random.randint(1,8)
	if choice == 1:
		answer=ans1
	elif choice == 2:
		answer=ans2
	elif choice == 3:
		answer=ans3
	elif choice == 4:
		answer=ans4
	elif choice == 5:
		answer=ans5
	elif choice == 6:
		answer=ans6
	elif choice == 7:
		answer=ans7
	else:
		answer=ans8
		
	print(answer)
	input("\n\nif you want")
	
if __name__ == '__main__':
	main()