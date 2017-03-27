#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import logging

log_file = './realtime.log'
log_level = 'DEBUG'
log_format = '[%(asctime)s: %(levelname)s/%(module)s] %(message)s'
logging.basicConfig(stream=open(log_file, 'a'), level=log_level,
                    format=log_format)
url = "http://www.naver.com"

html_result = requests.get(url)
bs = BeautifulSoup(html_result.text, "html.parser")

li_up = bs.find_all("li",class_=True,value=True)
for a in li_up:
    real=a.find("span",{"class":"ell"})
    try:
        logging.info(a['value']+u"등" + u" "+ real.text)
    except:
        pass