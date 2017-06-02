# -*- coding:utf-8 -*-

def main():
    try:
        f = open('nofile.txt','r')
        data = f.read()
        print(data)

#        4/0
    except FileNotFoundError as e:
        print("You need to create the file : %s" % e)
    else:
        f.close()
    finally:
        print("we done O.K")
        
#    except ZeroDivisionError:
#        print("Please check your division")
#    4/0
#    a = [1,2,3]
 #   print(a[2])
if __name__ == '__main__':
    main()