# -*- coding:utf-8 -*-

# try..except 실습 2

def main():
    try:
        f = open('nofile.txt', 'r')
#        4/0
    except FileNotFoundError:
        print("You need to create the file")
    
if __name__ == '__main__':
    main()
