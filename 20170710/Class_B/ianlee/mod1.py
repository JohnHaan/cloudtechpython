def sum(a,b):
    return a+b

def safe_sum(a,b):
    if type(a) != type(b):
        print ("cant")
        return
    else:
        return a+b
        
if __name__ == "__main__":

# if 아래가 import mod1 하면 안나오고, python mod1.py 하면 나오고

    print (sum(1,2))
    print (safe_sum(1,'a'))


