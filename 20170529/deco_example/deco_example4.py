#### 데코레이터를 활용해서 함수가 수행되기 전,후의 시간을 남기기

# -*- coding:utf-8 -*-

from datetime import datetime

def check_time(func):
    def wrapper():
        print(datetime.now())
        func()
        print(datetime.now())
    return wrapper()

@check_time
def create():
    print("creating instance..")

@check_time
def reboot():
    print("rebooting instance..")
 
@check_time
def stop():
    print("stopping instance..")