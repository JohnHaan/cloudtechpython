def sum(a,b):
    return a+b

def safe_sum(a,b):
    if type(a) != type(b):
        print ("cant")
        return
    else:
        return a+b
        
