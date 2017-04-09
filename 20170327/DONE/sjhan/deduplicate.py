# -*- coding:utf-8 -*-

def dedupe(targets):
    resList = []
    for target in targets:
        if target not in resList:
            resList.append(target)
    return resList

def dedupe_dict(targets):
    resList = []
    for target in targets:
        same = False
        if len(resList) == 0:
            resList.append(target)
        for resDict in resList:
            if target.get('x') == resDict.get('x') and target.get('y') == resDict.get('y'):
                same = True
        if not same:
            resList.append(target)
    return resList

def main(targets):
    element = targets[0]
    if isinstance(element, str) or isinstance(element, int):
        return dedup(targets)
    if isinstance(element, dict):
        return dedupe_dict(targets)

if __name__ == '__main__':
    a = [1,2,2,4,5,5,9]
    b = ['apple', 'banana', 'kiwi', 'banana', 'melon', 'apple']
    c = [{'x': 2, 'y': 3}, {'x': 1, 'y': 4}, {'x': 2, 'y': 3}, {'x': 2, 'y': 3}, {'x': 10, 'y': 15}]
    res = main(c)
    print(res)