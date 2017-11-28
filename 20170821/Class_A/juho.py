from pprint import pprint

#my_dict = { 'result': True, 'records': [ { 'id': 1, 'value': 'First Value' }, { 'id': 2, 'value': 'Second Value' } ], 'count': 2 }
#pprint(my_dict)

#a_list = [[1, 2], [3, 4], [5, 6, [7,8,9] ]]
#print(list(itertools.chain.from_iterable(a_list)))

class A(object):
    def __init__(self, a, b, c, d, e, f):
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})
        
