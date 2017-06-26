from datetime import datetime


def check_date():
    '''
    with open("/projects/cloudtechpython/20170605/LOGS/master.log", "a") as f:
        snow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(snow + "\n")
    '''
    return

def main():
    check_date()

def year():
    d = datetime.today()
    print(d.year)
    return

def month():
    d = datetime.today()
    print (d.month)
    return

def date():
    d = datetime.today()
    print (d.day)
    return

def time():
    d = datetime.today()
    print (d.hour)
    return

if __name__ == '__main__':
    main()