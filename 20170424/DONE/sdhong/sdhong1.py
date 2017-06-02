import os

def main():

    path = "./sdhong/test"
    try: 
        os.makedirs(path)
        #os.mkdir(path)
    except OSError as e:
        print(e)
    
if __name__ == '__main__':
    main()