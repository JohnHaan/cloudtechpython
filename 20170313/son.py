# -*- coding:utf-8 -*-

import os
import requests
import sys

def main():
	#r = requests.get('https://api.github.com/events')
	url = 'http://www.daum.net/get'
	payload = {'key1':'value1', 'key2':'value2'}
	r = requests.post(url, data=payload)
	print(r.text)
	
if __name__ == '__main__':
	main()