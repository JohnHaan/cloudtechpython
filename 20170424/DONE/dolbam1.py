import os

def main():

    path = "./dolbam2"
    try: 
        os.makedirs(path)
    except OSError as e:
        print(e)
    
if __name__ == '__main__':
    main()
    