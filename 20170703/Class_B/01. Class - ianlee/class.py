클래스 에 의해 생기는 것이 인스턴스
클래스란 인스턴스를 만들어내는 공장

class Simple:
    pass

a = Simple()

Simple = 클래스
a = 인스턴스



class Service:
    secret = "영구는 배꼽이 두 개다"
    def setname(self, name):
    self.name = name
    def sum(self, a, b):
    result = a + b
    print ("%s님 %s + %s = %s입니다.") % (self.name, a, b, result)
    

pey = Service()
pey.name = "이창재"
pey.sum(1,2)





class Service:
    secret = "영구는 배꼽이 두 개다"
    def __init__(self, name):
    self.name = name
    def sum(self, a, b):
    result = a + b
    print ("%s님 %s + %s = %s입니다.") % (self.name, a, b, result)
    
pey = Service("이창재")
pey = sum(1,2)


class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(1,2)
a.sum()
a.mul()
a.sub()
a.div()

class HousePark:
    lastname = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print "%s, %s여행을 가다." % (self.fullname, where)
    def __del__(self):
        print "%s 죽네 % self.fullname

a = HousePark("근혜")
del a


class HouseKim(HousePark):
    lastname = "김“
    def travel(self, where, day):
        print "%s, %s여행 %d일 가네." % (self.fullname, where, day)


b = HouseKim("정은")
b.travel("미국",3)
del b




class HousePark:
    lastname = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print "%s, %s여행을 가다." % (self.fullname, where)
    def love(self, other):
        print "%s, %s 사랑에 빠졌네" % (self.fullname, other.fullname)
    def fight(self, other):
        print "%s, %s 싸우네" % (self.fullname, other.fullname)
    def __add__(self, other):
        print "%s, %s 결혼했네" % (self.fullname, other.fullname)
    def __sub__(self, other):
        print "%s, %s 이혼했네" % (self.fullname, other.fullname)
    def __del__(self):
        print "%s 죽네" % self.fullname

class HouseKim(HousePark):
    lastname = "김"
    def travel(self, where, day):
        print "%s, %s여행 %d일 가네." % (self.fullname, where, day)

a = HousePark("근혜")
b = HouseKim("정은")
a.travel("미국")
b.travel("미국,3")
a.love(b)
a+b



