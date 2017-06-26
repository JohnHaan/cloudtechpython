#def test_var_args(f_arg, *argv):
#    print("first normal arg:", f_arg)
#    for arg in argv:
#        print("another arg through *argv:", arg)
#
#test_var_args('yasoob', 'python', 'eggs', 'test')


#def greet_me(*args, **kwargs):
#    for a in args:
#        print(a)
#    for key, value in kwargs.items():
#        for a in args:
#            print("{0} = {1}, {2}".format(key, value, a))
#
#greet_me(17, name="yasoob")


#def generator_function():
#    for i in range(10):
#        yield i
#
#for item in generator_function():
#    print(item)


#def fibon(n):
#    a = b = 1
#    for i in range(n):
#        yield a
#        a, b = b, a + b
#
#for x in fibon(100):
#    print(x)


def generator_function():
    for i in range(3):
        yield i

gen = generator_function()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


