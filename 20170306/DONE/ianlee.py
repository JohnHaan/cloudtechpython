#-*- coding:utf-8 -*-
	
"""문제 1. 다음(Daum)의 주가가 89,000원이고 네이버(Naver)의 주가가 751,000이라고 가정하고, 어떤 사람이 다음 주식 100주와 네이버 주식 20주를 가지고 있을 때 그 사람이 가지고 있는 주식의 총액을 계산하는 프로그램을 작성하세요.
- 조건: 2개 이상의 함수를 사용할 것, 결과값은 천 단위마다 쉼표가 들어갈 것(예> 764,000)"""

# Daum = 89000
# Naver = 751000

# n= Daum*100 + Naver*20
# m= format(n, ",d")

# print(m)


"""문제 2. 55페이지 아이디어 2"""

import random

computer_number = random.randint(1, 100)

def is_same(target, number):

	if target == number:

		result="Win"		
	elif target > number:

		result="Low"
	else:

		result="High"
	return result



print ("안녕. \n 난 1부터 100 중 숫자 하나를 골랐어요.")

guess = int(input("뭔지 쓰고 엔터 키를 누르세요."))
counter = 1
higher_or_lower = is_same(computer_number, guess)


while higher_or_lower != "Win":
	print(counter,"회")
	counter = counter+1
	if higher_or_lower == "Low":
#		counter = counter+1
		guess = int(input("그것보단 높습니다. 다시 생각해보세요."))		
#		print(counter,"회")
	else:
#		counter = conuter+1
		guess = int(input("그것보단 낮습니다. 다시 생각해보세요."))        
#		print(counter,"회")
	higher_or_lower = is_same(computer_number, guess)

print(counter,"회")
input("정답\n잘했어요.\n\n\n마치려면 엔터키를 누르세요.")




"""문제 3. 56페이지 아이디어 4"""

# import random


# level = input("레벨골라 emh\n")

# #print(is_level(level))

# while level != "e" and level != "m" and level !="h":
# 	level = input("다시넣어\n")
	
# def is_level(grade):
# 	if grade == "e":
# 		limit = 10
# 	elif grade == "m":
# 		limit = 20
# 	else:
# 		limit = 100
# 	return limit

# n=is_level(level)


# computer_number = random.randint(1, int(n))

# def is_same(target, number):
# 	if target == number:
# 		result ="Win"
# 	elif target > number:
# 		result="Low"
# 	else:
# 		result="High"
# 	return result

# print ("안녕. \n 난 1부터", n, "중 숫자 하나를 골랐어요.")

# guess = int(input("뭔지 쓰고 엔터 키를 누르세요."))

# higher_or_lower = is_same(computer_number, guess)

# while higher_or_lower != "Win":
# 	if higher_or_lower == "Low":
# 		guess = int(input("그것보단 높습니다. 다시 생각해보세요."))
# 	else:
# 		guess = int(input("그것보단 낮습니다. 다시 생각해보세요."))
# 	higher_or_lower = is_same(computer_number, guess)
		
# input("정답\n잘했어요.\n\n\n마치려면 엔터키를 누르세요.")
 
		

"""문제 4. 'netmarblegames'라는 문자열의 각 알파벳의 갯수를 저장하는 프로그램을 작성하세요.
- 예> 'banana' => {'a': 3, 'b': 2, 'n': 2}
- hints: 문자열의 각 알파벳 별로 반복문을 수행하려면..
        for i in 'abc':
            print(i)
- hints : 빈 dictionary 정의..
        dict = {}	"""

# s="netmarblegames"

# #dict={}


# for i in "netmarblegames":
# 	print(i,"=",s.count(i))


	
