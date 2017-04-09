def eliminator(target):
    newlist=[]
    for e in target:
        if(newlist.count(e) == 0):
            newlist.append(e)

    return newlist

def main():
    listA = [1, 5, 2, 1, 9, 1, 5, 10]
    listB = ['apple', 'banana', 'kiwi', 'banana', 'melon', 'apple']
    listC = [{'x': 2, 'y': 3}, {'x': 1, 'y': 4}, {'x': 2, 'y': 3}, {'x': 2, 'y': 3}, {'x': 10, 'y': 15}]
    newA = eliminator(listA)
    newB = eliminator(listB)
    newC = eliminator(listC)
    print(newA)
    print(newB)
    print(newC)

if __name__ == '__main__':
    main()