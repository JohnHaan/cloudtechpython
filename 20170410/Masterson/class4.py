class Service:
    def __init__(self, name):
        self._secret="test"
        self.name = name
    def sum(self, a, b):
        result = a+b
        print("%s %d + %d = %d" % (self.name,a,b,result))
    
pey = Service("Master Son")
print(pey._secret)
pey.sum(1,2)
#Service.sum(pey,1,5)