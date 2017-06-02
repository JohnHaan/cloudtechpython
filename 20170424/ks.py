# -*- coding:utf-8 -*-

# 일반적인 에러

def main():
    try:
        f = open('nofile.txt', 'r')
    except FileNotFoundError:
        print("you need to create file")
    except ZeroDivisionError as e:
        print("please check your division:%s" % e)
    except Exception:
        pass
    else:
        print(f.read())
    finally:
        f.close()
        print("done")

class Bird(object):
    def __init__(self):
        pass
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def __init__(self):
        super(Eagle, self).__init__()
    def fly(self):
        print("I can fly")
        
class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

def say_nick(nick):
    if nick == 'dolbam':
        raise MyError("wrong nick!!!")

if __name__ == '__main__':
    # main()
    eagle = Eagle()
    eagle.fly()
    for i in ["a", 'dolbam']:
        try:
            print(i)
            say_nick(i)
        except MyError as e:
            print("wrong nick:%s" % e)
