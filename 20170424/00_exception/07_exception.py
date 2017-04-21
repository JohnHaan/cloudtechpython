# -*- coding:utf-8 -*-

# try..except 실습 5

def main():
    try:
        f = open('foo.txt', 'r')
        data = f.read()
        print(data)
    except FileNotFoundError as e:
        print(str(e))
    else:
        f.close()
    finally:
        print("Ok We done.")
    
if __name__ == '__main__':
    main()