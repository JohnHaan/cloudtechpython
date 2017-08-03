
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        return "very fast"

#a=Bird()
#print(a.fly())

b=Eagle()
print(b.fly())
