# -*- coding:utf-8 -*-

# try..except 실습 4

def main():
    try:
        f = open('nofile.txt', 'r')
    except FileNotFoundError as e:
        print("Something wrong : %s" % e)
    
if __name__ == '__main__':
    main()