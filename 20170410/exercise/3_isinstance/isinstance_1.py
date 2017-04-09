# -*- coding:utf-8 -*-

## 클래스 객체와 인스턴스 객체의 관계

class Person(object):
    pass

class Bird(object):
    pass

class Student(Person):
    pass
    
p, b, s = Person(), Bird(), Student()

print("p is instance of Person: ", isinstance(p, Person))
print("p is instance of Bird: ", isinstance(p, Bird))
print("b is instance of Person: ", isinstance(b, Bird))
print("s is instance of Person: ", isinstance(s, Person))
print("s is instance of object: ", isinstance(s, object))

