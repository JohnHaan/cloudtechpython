# -*- coding:utf-8 -*-

class Service(object):
    def __init__(self, name):
        self._secret = "영구는 배꼽이 없다."
        self.name = name
        
    def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s입니다." % (self.name, a, b, result))
        
#pey = Service("김영노")
#print(pey._secret)
#pey.sum(1, 1)

class MyClass(object):
    def __init__(self, value):
        self.value = value
        print("Class is created! Value = ", value)
        
    def __del__(self):
        print("Class is deleted!")
        
#foo = MyClass(1)

class Person(object):
    pass

class Bird(object):
    pass
    
class Student(Person):
    pass

p = Person()
b = Bird()
s = Student()

print("p is instance of Person: ", isinstance(p, Person))
print("p is instance of Bird: ", isinstance(p, Bird))
print("b is instance of Person: ", isinstance(b, Bird))
print("s is instance of Person: ", isinstance(s, Person))
print("s is instance of object: ", isinstance(s, object))
