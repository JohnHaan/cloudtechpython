#import collections
#import json

#tree = lambda: collections.defaultdict(tree)

#somedict = tree()
#somedict['colours']['favourite']['zeroxkim'] = "yellow"

#print(somedict)
#print(json.dumps(somedict))



#from collections import OrderedDict

#colours = OrderedDict([("Red", 198), ("Green", 170), ("Blue", 160)])

#for key, value in colours.items():
#    print(key, value)



#from collections import Counter

#colours = (
#    ('Yasoob', 'Yellow'),
#    ('Ali', 'Blue'),
#    ('Arham', 'Green'),
#    ('Ali', 'Black'),
#    ('Yasoob', 'Red'),
#    ('Ahmed', 'Silver'),
#)

#favs = Counter(colour for name, colour in colours)

#print(favs)



#from collections import deque

#d = deque()

#d.append('1')
#d.append('3')
#d.append('2')

#print(len(d))
#print(d[0])
#print(d[-1])



#from collections import deque

#d = deque(range(5))

#print(len(d))

#d.popleft()
#d.pop()

#print(d)



#from collections import namedtuple

#animal = namedtuple('animal', 'name age type')
#perry = animal(name="perry", age=31, type="cat")

#print(perry)

#print(perry.name)



#my_list = ['apple', 'banana', 'grapes', 'pear']

#for c, value in enumerate(my_list, 1):
#    print(c, value)



a = {"k": [0, {"k2": "hello"}, 2] }
print(a["k"][1]["k2"])

