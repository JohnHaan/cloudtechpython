def main():
	# 문제 1. 다음(Daum)의 주가가 89,000원이고 네이버(Naver)의 주가가 751,000이라고 가정하고, 어떤 사람이 다음 주식 100주와 네이버 주식 20주를 가지고 있을 때 그 사람이 가지고 있는 주식의 총액을 계산하는 프로그램을 작성하세요.
	daum = 89000
	naver = 751000
	sum = daum * 100 + naver * 20

	print("A1 : %d" % sum)
	
	# 문제 2. 월요일에 넷마블의 주가가 100만 원으로 시작해 3일 연속으로 하한가(-30%)를 기록했을 때 수요일의 종가를 계산해 보세요.
	netmarble = 1000000
	#stock = netmarble * 0.7 * 0.7 * 0.7
	stock = netmarble * 
		
	print("A2 : %f" % stock)
	
	# 문제 3. 다음 형식과 같이 이름, 생년월일, 주민등록번호를 출력하는 프로그램을 작성해 보세요. 이름: 파이썬 생년월일: 2014년 12월 12일 주민등록번호: 20141212-1623210
	name = "파이썬"
	birthday = "2014년 12월 12일"
	rrn = "20141212-1623210"
	answer = "이름: %s 생년월일: %s 주민등록번호: %s" % (name, birthday, rrn)
	
	print("A3 : %s" % answer)
	
	# 문제 4. s라는 변수에 'Netmarble Games'라는 문자열이 바인딩돼 있다고 했을 때 문자열의 슬라이싱 기능과 연결하기를 이용해 s의 값을 'Games Netmarble'으로 변경해 보세요.
	s = "Netmarble Games"
	ns = s[10:] + s[9] + s[:9]
	
	print("A4 : %s" % ns)
	
	# 문제 5. a라는 변수에 'hello world'라는 문자열이 바인딩돼 있다고 했을 때 a의 값을 'hi world'로 변경해 보세요.
	a = "hello world"
	b = a.replace("hello", "hi")
	
	print("A5 : %s" % b)

	# 문제 6. x라는 변수에 'abcdef'라는 문자열이 바인딩돼 있다고 했을 때 x의 값을 'bcdefa'로 변경해 보세요.
	x = 'abcdef'
	y = x[1:] + x[0]
	
	print("A6 : %s" % y)

if __name__ == '__main__':
	main()
