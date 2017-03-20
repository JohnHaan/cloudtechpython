# -*- coding:utf-8 -*-

def main():
	# number 1
	daum = 89000
	naver = 751000
	total = daum*100 + naver*20
	print('문제 1번 답: {}'.format(total))
	
	# number 2
	netmarble = 1000000
	days = ['mon', 'tues', 'wednes']
	for i in xrange(len(days)):
		netmarble = 0.7*netmarble
	print('문제 2번 답: {}'.format(netmarble))

	# number 3
	name = '이름: %s' % '파이썬'
	birth = '생년월일: %s' % '2014년 12월 12일'
	idnum = '주민등록번호: %s' % '20141212-1623210'
	whois = name + ' ' + birth + ' ' + idnum
	print('문제 3번 답: {}'.format(whois))
	
	# nuber 4
	old_name = 'Netmarble Games'
	head = old_name[:9]
	tail = old_name[-5:]
	new_name = tail + ' ' + head
	print('문제 4번 답: {}'.format(new_name))
	
	# number 5
	a = 'Hello World'
	b = a[6:]
	a = 'Hi ' + b
	print('문제 5번 답: {}'.format(a))
	
	# number 6
	x = 'abcdef'
	y = x[1:]
	z = x[0]
	x = y+z
	print('문제 6번 답: {}'.format(x))
		
if __name__ == '__main__':
	main()