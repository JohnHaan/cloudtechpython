from datetime import datetime

def _put_time(fmt):
    print(datetime.now().strftime(fmt))
        
def what_year(fmt="%Y"):
    _put_time(fmt)

def what_month(fmt="%m"):
    _put_time(fmt)

def what_day(fmt="%d"):
    _put_time(fmt)

def what_time(fmt="%H:%M"):
    _put_time(fmt)

if __name__ == '__main__':
    what_year()
    what_day()
    what_time()
