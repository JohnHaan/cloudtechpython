# _*_ coding:utf-8 _*_

from datetime import datetime

def check_time(tag):
    def set_decorator(func):
        def wrapper():
            print("before %s method time check: %s" % (tag, datetime.now()))
            func()
            print("before %s method time check: %s" % (tag, datetime.now()))
        return wrapper()
    return set_decorator

@ check_time("create")
def create():
    print ("creating instances..")

@ check_time("reboot")    
def reboot():
    print ("rebooting instances..")

@ check_time("stop")    
def stop():
    print ("stoping instances..")