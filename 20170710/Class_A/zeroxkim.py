"""
7.1
""""""
def hi(name="yasoob"):
    return "hi " + name

print(hi())

greet = hi

print(greet())

del hi
try: print(hi())
except NameError: print("NameError")

print(greet())
"""

"""
7.2
""""""
def hi(name="yasoop"):
    print("now you are inside the hi() function")
    
    def greet():
        return "now you are in the greet() function"
        
    def welcome():
        return "now you are in ter welcome() function"
    
    print(greet())
    print(welcome())
    print("now you are back in the hi() function")

hi()

greet()
"""

"""
7.3
""""""
def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"
    
    def welcome():
        return "now you are in the welcome() function"
    
    if name == "yasoob":
        return greet
    else:
        return welcome

#a = hi()
a = hi("zeroxkim")
print(a)

print(a())
"""

"""
7.4
""""""
def hi():
    return "hi yasoop"

def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())

doSomethingBeforeHi(hi)
"""

"""
7.5
""""""
#def a_new_decorator(a_func):
#    def wrapTheFunction():
#        print("I am doing some boring work before executing a_func()")
#        a_func()
#        print("I am doing some boring work after executing a_func()")
#    
#    return wrapTheFunction

#def a_function_requiring_decoration():
#    print("I am the function which needs some decoration to remove my foul smell")

#a_function_requiring_decoration()

#a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

#a_function_requiring_decoration()


#def a_new_decorator(a_func):
#    def wrapTheFunction():
#        print("I am doing some boring work before executing a_func()")
#        a_func()
#        print("I am doing some boring work after executing a_func()")
#    
#    return wrapTheFunction

#@a_new_decorator
#def a_function_requiring_decoration():
#    print("I am the function which needs some decoration to remove my foul smell")

#a_function_requiring_decoration()


#from functools import wraps

#def a_new_decorator(a_func):
#    @wraps(a_func)
#    def wrapTheFunction():
#        print("I am doing some boring work before executing a_func()")
#        a_func()
#        print("I am doing some boring work after executing a_func()")
#    
#    return wrapTheFunction

#@a_new_decorator
#def a_function_requiring_decoration():
#    print("I am the function which needs some decoration to "
#          "remove my foul smell")

#print(a_function_requiring_decoration.__name__)


#from functools import wraps

def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        
        return f(*args, **kwargs)
    
    return decorated

@decorator_name
def func():
    return("Function is running")

can_run = True
print(func())

can_run = False
print(func())
"""

"""
8.1
""""""
def profile():
    name = "Danny"
    age = 30
    
    return (name, age)

profile_data = profile()
print(profile_data[0])

print(profile_data[1])

a, b = profile()
print("%s, %s" % (a, b))
"""


