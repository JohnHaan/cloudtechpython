class person(object):
    pass
    
class bird(object):
    pass
    
class son(person):
    pass 
    
p, b, s = person(), bird(), son()

print("p is instance of Person: ", isinstance(p, person))
print("p is instance of Bird: ", isinstance(p, bird))
print("b is instance of Person: ", isinstance(b, bird))
print("s is instance of Person: ", isinstance(s, person))
print("s is instance of object: ", isinstance(s, object))