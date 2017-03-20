# -*- coding:utf-8 -*-

### 1. 내장 라이브러리
# sys
import sys
sys.path
sys.path.append('/workspace/pythonstudy01/20170313')
sys.path
import {name}.py

# os
import os
os.getcwd()
os.chdir('sjhan')
os.getcwd()
os.listdir('.')
os.makedirs()
os.rmdir('sjhan')
os.listdir()

### 2. 외부 라이브러리
pip install --upgrade pip

import requests
r = requests.get('https://api.github.com/events')
r.status_code
r.headers['Content-Encoding']
r.encoding
r.text
r.json()

# headers
url = 'https://api.github.com/events'
headers = {'Content-type': 'json'}
r = requests.get(url, headers=headers)

# POST
url = 'http://httpbin.org/post'
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post(url, data=payload)
print(r.text)
