class MyError(Exception):
    pass
    
def say_nick(nickname):
    if nickname == 'dolbam':
        raise MyError()
    print(nickname)
    
if __name__ == '__main__':
    for i in ['zeroxkim', 'dolbam']:
        try:
            say_nick(i)
        except MyError:
         print("wrong nickname")