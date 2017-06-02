# -*- coding:utf-8 -*-

def main():
#    try:
#        f = open("nofile.txt", "r")
#        data = f.read()
#        print(data)
#        #4/0
#        #a = [1, 2, 3]
#        #print(a[4])
#    except FileNotFoundError as e:
#        print("Something wrong : %s" % e)
#    except ZeroDivisionError:
#        print("Not division by zero")
#    else:
#        f.close()
#    finally:
#        print("OK We done")
    
    eagle = Eagle()
    eagle.fly()

class Bird(object):
    def __init__(self):
        pass
        
    def fly(self):
        raise NotImplementedError   # must except
        
class Eagle(Bird):
    def __init__(self):
        super(Eagle, self).__init__()
        pass
        
    def fly(self):
        print("I believe I can fly")
        
if __name__ == '__main__':
    main()
    