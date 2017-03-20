# -*- coding:utf-8 -*-

import requests


def main():
	r = requests.get("https://api.github.com/events")
	print(r.headers)
	print(r.encoding)
	print(r.text)
	print(r.json())
	r = requests.post("http://httpbin.org", data={"key1": "val1", "key2": "val2"})
	print(r.text)

if __name__ == '__main__':
	main()
