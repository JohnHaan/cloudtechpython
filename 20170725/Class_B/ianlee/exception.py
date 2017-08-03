# try:
# except [발생에러]:

#def main():
#    try:
#        f = open('nofile.txt', 'r')
#        4/0
#    except FileNotFoundError:
#        print("You need to create the file")
#    except ZeroDivisionError:
#        print("Please check your division")
#    
#if __name__ == '__main__':
#    main()

#====================================================

# except [발생에러] as [에러메세지 변수]:
# except [발생에러], [에러메세지 변수]: <- 안됨


#def main():
#    try:
#        f = open('nofile.txt', 'r')
#    except FileNotFoundError as a:
#        print("Something wrong : %s" % a)
#    
#if __name__ == '__main__':
#    main()
    
#=====================================================    
# try:
# except:
# else:
    
#def main():
#    try:
#        f = open('foo.txt', 'r')
#    except FileNotFoundError as e:
#        print(str(e))
#    else:
#        data = f.read()
#        print(data)
#        f.close()
#    
#if __name__ == '__main__':
#    main()

#=====================================================
# try:
# except:
# else:
# finally:

#def main():
#    try:
#        f = open('foo.txt', 'r')
#        data = f.read()
#        print(data)
#    except FileNotFoundError as e:
#        print(e)
#    else:
#       f.close()
#    finally:
#        print("Ok We done.")
#    
#if __name__ == '__main__':
#    main()

#=======================================================

#class MyError(Exception):
#    pass
#    
#def say_nick(nickname):
#    if nickname == 'dolbam':
#        raise MyError()
#    print(nickname)
#
#if __name__ == '__main__':
#    for i in ['zeroxkim', 'dolbam']:
#        try:
#            say_nick(i)
#        except MyError:
#            print("wrong nickname")

#========================================================

#class MyError(Exception):
#    def __str__(self):
#        return "허용되지 않는 별명입니다."
#        
#def say_nick(nickname):
#    if nickname == 'dolbam':
#        raise MyError()
#    print(nickname)
#
#if __name__ == '__main__':
#    for i in ['zeroxkim', 'dolbam']:
#        try:
#            say_nick(i)
#        except MyError:
#            print(MyError.__dict__)

#========================================================

#class MyError(Exception):
#    def __init__(self, msg):
#        self.msg = msg
#
#    def __str__(self):
#        return self.msg
#    
#    
#def say_nick(nickname):
#    if nickname == 'dolbam':
#        raise MyError('잘못된 별명임.')
#    print(nickname)
#
#if __name__ == '__main__':
#    for i in ['zeroxkim', 'dolbam']:
#        try:
#            say_nick(i)
#        except MyError as e:
#            print(e)
           