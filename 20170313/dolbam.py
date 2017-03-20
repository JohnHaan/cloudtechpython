# -*- coding:utf-8 -*-
import requests

#import main_sample

def main():
	r=requests.get('http://naver.com')
	print(r)
	print(type(r))
	print(r.status_code)
	print(r.headers['Content-Encoding'])
	print(r.encoding)
	
if __name__ == '__main__':
	main()