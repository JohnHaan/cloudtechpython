
class Service(object):
    secret = "secret!"
    
    def sum(self, a, b):
        result = a + b
        print("%s: %s + %s = %s" % (self, a, b, result))


pey = Service()
print(pey.secret)

pey.sum(1,1)
Service.sum(pey,1, 1)
