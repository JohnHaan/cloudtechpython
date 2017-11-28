test_list=[1,2,3,4]
print(dir(test_list))

test_list.append([5,6])
print(test_list.reverse())


print(test_list)

print(dir(''))
print(type([]))
print(type(()))
print(type({}))
print(type(dict))
print(type(str))

print(__name__) 

import inspect

print(inspect.trace(inspect))

multiples = [i for i in range(1,30) if i % 3 == 0]
print(multiples)

mcase = {'a':10, 'b':34, 'A':33, 'Z': 3}
mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
}
print(mcase_frequency)

a = {v: k for k, v in mcase_frequency.items()}
print(a)


squared = {x**2 for x in [1,1,3,4]}
print(squared)



a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
print(a)