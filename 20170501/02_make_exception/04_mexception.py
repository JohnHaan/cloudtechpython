class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
    
def say_nick(nickname):
    if nickname == 'dolbam':
        raise MyError('잘못된 별명임.')
    print(nickname)

if __name__ == '__main__':
    for i in ['zeroxkim', 'dolbam']:
        try:
            say_nick(i)
        except MyError as e:
            print(e)