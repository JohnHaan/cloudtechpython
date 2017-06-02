import os

def main():

    path = "./new"
    try: 
        os.makedirs(path)
    except OSError as e:
        print(e)
    
if __name__ == '__main__':
    main()