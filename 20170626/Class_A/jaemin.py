def test_var_args(f, *args):
    print("first normal arg:", f)
    for arg in args:
        print("another arg through *args:", arg)
        
        
#test_var_args('1', '2', '3', '4')

def greet_me(level, *args, **kwargs):
    print("%s level" % level)
    for a in args:
        print("age: ", a)
    for key, value in kwargs.items():
        print("{0} = {1}".format(key,value))
        
#greet_me(11, 19, name='test')

def generator_func():
    for i in range(10):
        yield i
        
for item in generator_func():
    print(item)

def generator_function():
    for i in range(3):
        yield i
        
gen = generator_function()
print("test: ", next(gen))
print("test: ", next(gen))
print("test: ", next(gen))



