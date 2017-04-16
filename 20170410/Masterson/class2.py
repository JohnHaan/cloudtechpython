r1=0
r2=0

def adr1(num):
    global r1
    r1 +=num
    return r1
    
def adr2(num):
    global r2
    r2 += num
    return r2

print(adr1(1))
print(adr2(3))