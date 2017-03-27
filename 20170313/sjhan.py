# -*- coding:utf-8 -*-

import requests

#print('Hello World')

def main():
	url = 'http://httpbin.org/post'
	payload = {'key1': 'value1', 'key2': 'value2'}
	r = requests.post(url, data=payload)
	print(r.conten)

if __name__ == '__main__':
	main()