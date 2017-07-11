items = [1, 2, 3, 4, 5]
squared = list()

for i in items:
    squared.append(i**2)

print("for loop: ", squared)

sqad = list(map(lambda x: x**2, items))
print("map func: ", sqad)

number_list = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5, 0]
less_than_zero = list(filter(lambda x: x>=0, number_list))
print("filter func: ", less_than_zero)


from functools import reduce

product = reduce((lambda x, y: x*y), [1,2,3,4])
print(product)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)

valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.intersection(valid))

#연산자 오버라이딩
print(valid & input_set)
print(valid | input_set)
print(valid - input_set)
print(valid ^ input_set)


is_fat = True
state = "fat" if is_fat else "not fat"
print(state)

fat = True
# ( false, true ) = ( 0, 1 )
fitness = ("skinny", "fat")[fat]
print("Ali is ", fitness)


