import string

def problem1():
	daumstock = 89000
	naverstock =  751000	

	someonedaumcount = 0
	someonenavercount = 0

	someonedaumcount = input("input daumstock count : ")
	someonenavercount = input("input naverstock count : ")
	
	daumvalue = daumstock * someonedaumcount
	navervalue = naverstock * someonenavercount
	print("Total stock Value : %d", daumvalue+navervalue )
	
def problem2():
	stockvalue = 1000000
	cnt=3
	while(cnt>0):
		cnt=cnt-1
		stockvalue = stockvalue * 0.7
	
	print("stockvalue : %d", (int)(stockvalue))
	
def problem3():
	name = raw_input("input name : ")
	birthyear = raw_input("input birth Year : ")
	birthmonth = raw_input("input birth month: ")
	birthday = raw_input("input birth day: ")
	sdnum = raw_input("input Ident Number:")
	someone = "name : "+name+" birth: "+birthyear+" Year"+birthmonth+" Month "+birthday+"Day "+"IDNUM : "+sdnum
	print (someone)
	
def problem4():
	s = "Netmarble Games"
	front = s[0:9]
	end = s[10:]
	print(end+" "+front)

	
def problem5():
	a = "hello world"
	a = "hi"+a[5:]
	print(a)
	
	
def problem6():
	x = "abcdef"
	x = x[1:]+x[0]
	print(x)
	
if __name__ == '__main__':
	#problem1()
	#problem2()
	#problem3()
	#problem4()
	#problem5()
	problem6()