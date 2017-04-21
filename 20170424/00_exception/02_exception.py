# -*- coding:utf-8 -*-

# try..except 실습 1

def main():
    try:
        f = open('nofile.txt', 'r')
    except:
        print("You need to create the file")
    
if __name__ == '__main__':
    main()

