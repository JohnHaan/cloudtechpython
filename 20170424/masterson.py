def main():
    #f = open("nofile.txt", 'r')
#    4/0
#    a = [1,2,3]
#    print(a[3])
    try:
        f = open('nofile.txt','r')
        data = f.read()
        print(data)
#        4/0
    except FileNotFoundError as e:
        print(str(e))
    else:
        f.close()
    finally:
        f.close()
        print("straight")
if __name__ == '__main__':
    main()