try:
    f=open("ddd.txt",'r')
except IOError:
    print("write mode.")
    f=open("ddd.txt",'w')

# FileNotFoundError: [Errno 2] No such file or directory: 'aaa.txt'
# IOError 인가?