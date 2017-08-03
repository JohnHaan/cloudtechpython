# -*- coding:utf-8 -*-

# try..except 실습 4

def main():
    try:
        f = open('foo.txt', 'r')
    except FileNotFoundError as e:
        print(str(e))
    else:
        data = f.read()
        print(data)
        f.close()
    
if __name__ == '__main__':
    main()

