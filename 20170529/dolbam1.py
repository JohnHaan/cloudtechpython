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
    
    
    
##
1. 인스턴스의 action을 수행 시, 인스턴스가 lock인지 확인하는 decorator 함수를 정의하라.
  - class instance 객체의 속성을 정의한다. ( name, lock여부)
  - instance 객체의 내장함수로 reboot과 stop을 정의한다.
  - reboot과 stop 함수 호출 시 lock 여부를 확인하고 lock일 경우 exception을 raise 시키는 함수를 정의한다.
  
  def is_lock(fu)
  
  class Instance(object):
    self.name = name
    self.is_lock = False
    
    def reboot():
        print()
        
    def stop():
        