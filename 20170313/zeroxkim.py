# -*- coding:utf-8 -*-

#import os
#import sys
import requests

#print('Hello World')

def main():
	#print('한글 테스트')
	#sys.path.append('/workspace/pythonstudy01/20170313')
	#print(sys.path)
	#os.chdir('DONE')
	#print(os.getcwd())
	#os.makedirs('zeroxkim')
	#os.rmdir('zeroxkim')
	#print(os.listdir('.'))
	
	#r = requests.get('https://api.github.com/events')
	#print(r.status_code)
	#print(r.headers['Content-Encoding'])
	#print(r.encoding)
	#print(r.text)
	#print(r.json())
	
	#url = 'http://api.github.com/events'
	#headers = {'Content-type': 'json'}
	#r = requests.get(url, headers=headers)
	#print(r.text)
	
	url = 'http://httpbin.org/post'
	payload = {'key1': 'value1', 'key2': 'value2'}
	r = requests.post(url, data=payload)
	print(r.text)
	#pass
	
if __name__ == '__main__':
	main()
	