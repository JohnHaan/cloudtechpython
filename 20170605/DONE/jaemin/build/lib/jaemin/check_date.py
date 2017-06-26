from datetime import datetime

def what_year():
    year = datetime.now().strftime("%Y")
    print ("year : %s" % year)

def what_month():
    month = datetime.now().strftime("%m")
    print ("month : %s" % month)

def what_date():
    date = datetime.now().strftime("%d")
    print ("date : %s" % date)

def what_time():
    time = datetime.now().strftime("%H:%M:%S")
    print ("time : %s" % time)
    
    
#if __name__ == '__main__':
#    what_year()
#    what_month()
#    what_date()
#    what_time()