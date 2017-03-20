# -*- coding:utf-8 -*-

import requests

def main():
	url = "http://httpbin.org/post"
	payload = {"key1": "value1", "key2":"value2"}
	r = requests.post(url, data=payload)
	print(r.text)
	
if __name__ == '__main__':
	main()