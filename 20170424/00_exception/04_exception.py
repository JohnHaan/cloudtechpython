# -*- coding:utf-8 -*-

# try..except 실습 3

def main():
    try:
        f = open('nofile.txt', 'r')
#        4/0
    except FileNotFoundError:
        print("You need to create the file")
    except ZeroDivisionError:
        print("Please check your division")
    
if __name__ == '__main__':
    main()