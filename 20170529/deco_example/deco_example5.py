#### 데코레이터를 활용해서 함수가 수행되기 전,후의 시간을 남기기

# -*- coding:utf-8 -*-

from datetime import datetime

def check_time(tag):
    def set_decorator(func):
        def wrapper():
            print("before %s method time check: %s" % (tag, datetime.now()))
            func()
            print("before %s method time check: %s" % (tag, datetime.now()))
        return wrapper()
    return set_decorator
    
@check_time("create")
def create():
    print("creating instance..")

@check_time("reboot")
def reboot():
    print("rebooting instance..")
 
@check_time("stop")
def stop():
    print("stopping instance..")
    