from datetime import datetime

def what_year():
    print(datetime.now().strftime("%Y"))
    
def what_month():
    print(datetime.now().strftime("%m"))
    
def what_date():
    print(datetime.now().strftime("%d"))

def what_time():
    print(datetime.now().strftime("%H:%M:%S"))
