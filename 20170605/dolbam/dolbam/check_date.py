from datetime import datetime


def check_date():
    with open("/projects/cloudtechpython/20170605/dolbam/example2.log", "a") as f:
        snow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(snow+"\n")

def main():
    check_date()
    
#if __name__=='__main__':
#    main()