from datetime import datetime

snow = datetime.now()

def what_year():
    print(snow.strftime('%Y'))

def what_month():
    print(snow.strftime('%m'))

def what_date():
    print(snow.strftime('%d'))

def what_time():
    print(snow.strftime('%H:%M:%S'))