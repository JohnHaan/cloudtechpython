import operator

def main():
	#문제 1. 다음(Daum)의 주가가 89,000원이고 네이버(Naver)의 주가가 751,000이라고 가정하고, 어떤 사람이 다음 주식 100주와 네이버 주식 20주를 가지고 있을 때 그 사람이 가지고 있는 주식의 총액을 계산하는 프로그램을 작성하세요.
	#  - 조건: 2개 이상의 함수를 사용할 것, 결과값은 천 단위마다 쉼표가 들어갈 것(예> 764,000)
	daum = 89000
	naver = 751000
	daum_stock = 100
	naver_stock = 20
	
	stock_total = sum(multifly(daum, daum_stock), multifly(naver, naver_stock))
	total = format(stock_total, ',')
		
	print("A1 : %s" % total)

#문제 2. 55페이지 아이디어 2
	# zeroxkim2.py

#문제 3. 56페이지 아이디어 4
	# zeroxkim3.py

#문제 4. 'netmarblegames'라는 문자열의 각 알파벳의 갯수를 저장하는 프로그램을 작성하세요.
#  - 예> 'banana' => {'a': 3, 'b': 2, 'n': 2}
#  - hints: 문자열의 각 알파벳 별로 반복문을 수행하려면..
#		for i in 'abc':
#			print(i)
#  - hints : 빈 dictionary 정의..
#  		dict = {}
	dict = {}
	
	for i in 'netmarblegames':
		if i in dict:
			dict[i] = dict[i] + 1
		else:
			dict[i] = 1
	
	sort = sorted(dict.items(), key=operator.itemgetter(0))
	
	print("A4 : %s" % sort)
	

def multifly(a, b):
	multifly_result = a * b
	return multifly_result
	
def sum(a, b):
	sum_result = a + b
	return sum_result
	

if __name__ == '__main__':
	main()
