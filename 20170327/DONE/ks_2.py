import cPickle

def del_duplication(list):
    return [cPickle.loads(s) for s in {cPickle.dumps(l) for l in list}]

if __name__ == '__main__':
    print(del_duplication(
        [1,5,2,1,9,1,5,10]))
    print(del_duplication(
        ['apple', 'banana', 'kiwi', 'banana', 'melon', 'apple']))
    print(del_duplication(
        [{'x': 2, 'y': 3}, {'x': 1, 'y': 4}, {'x': 2, 'y': 3},
         {'x': 2, 'y': 3}, {'x': 10, 'y': 15}]))