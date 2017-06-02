
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."
    
def say_nick(nickname):
    if nickname == 'dolbam':
        raise MyError()
    print(nickname)

if __name__ == '__main__':
    for i in ['zeroxkim', 'dolbam']:
        try:
            say_nick(i)
        except MyError as e:
            print(e)