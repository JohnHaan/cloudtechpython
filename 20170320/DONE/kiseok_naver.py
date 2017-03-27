#-*- coding: utf-8 -*-

import requests
from scrapy.selector import Selector

r = requests.get("http://www.naver.com")
results = Selector(text=r.text).xpath('//span[@class="ell"]/text()').extract()
with open("kiseok_naver.log", "a") as f:
    for r in results:
        f.write(r)
        f.write("\n" * 1)
    f.write("\n" * 1)
