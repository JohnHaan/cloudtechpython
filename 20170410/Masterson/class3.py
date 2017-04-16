class Cal(object):
    def __init__(self):
        self.result=0
        
    def addr(self, num):
        self.result += num
        return self.result
            
cal1 = Cal()
cal2 = Cal()

print(cal1.addr(3))
print(cal1.addr(5))
print(cal2.addr(2))
print(cal2.addr(3))