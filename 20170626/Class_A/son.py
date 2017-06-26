def test_var_args(f_arg, *args):
    print("first normal arg:", f_arg)
    for arg in args:
        print(arg)
        
def greet_me(*v, **ks):
    for k in v:
        print(k)
    for k, v in ks.items():
        print("{0} == {1}".format(k,v))
        
        
def generator_function():
    for i in range(10):
        yield(i)
        

for item in generator_function():
    print(item)
        
#greet_me(29, name="ysoop")
#greet_me()

#test_var_args('yasoob','python','eggs', 'test')
    