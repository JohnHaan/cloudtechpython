#### 데코레이터를 활용해서 함수가 수행되기 전,후의 시간을 남기기

# -*- coding:utf-8 -*-

from datetime import datetime

def check_time():
    print(datetime.now())
    
def create():
    check_time()
    print("creating instance..")
    check_time()

def reboot():
    check_time()
    print("rebooting instance..")
    check_time()
    
def stop():
    check_time()
    print("stopping instance..")
    check_time()

create()
reboot()
stop()