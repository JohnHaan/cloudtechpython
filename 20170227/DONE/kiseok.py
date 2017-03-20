#-*- coding: utf-8 -*-

#1
naver = 89000
daum = 751000
total = naver * 20 + daum * 100
print(total)

#2
netmarble = 1000000
for i in range(1,3):
	netmarble -= netmarble * 0.3
print(int(netmarble))

#3
print("이름: %s 생년월일: %d년 %d월 %d일 주민등록번호: %s" % (
	"파이썬", 2014, 12, 12, "20141212-1623210"))

#4
s = "Netmarble Games"
print (s[10:] + ' ' + s[:9])

#5
a = "hello world"
a = a.replace("hello", "hi")
print(a)

#6
x = "abcdef"
x = x[1:] + x[:1]
print (x)
