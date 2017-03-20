# -*- coding:utf-8 -*-
#import os
#import sys
import requests


#print('Hello World')

def main():
	#print(os.getcwd())
	#os.chdir('DONE')
	#print(os.listdir('.'))
	#os.makedirs('sdhong')
	#os.rmdir('sdhong')
	r = requests.get('https://api.github.com/events')
	print(r.status_code)
	print(r.headers['Content-Encoding'])
	print(r.encoding)
	print(r.text)
	print(r.json)
if __name__ == '__main__':
	main()