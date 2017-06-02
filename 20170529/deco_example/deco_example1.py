#### 데코레이터를 활용해서 함수가 수행되기 전,후의 시간을 남기기

# -*- coding:utf-8 -*-

from datetime import datetime

def create():
    print(datetime.now())
    print("creating instances..")
    print(datetime.now())

create()