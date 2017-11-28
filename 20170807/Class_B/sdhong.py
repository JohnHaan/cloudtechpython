#
#
#def main():
#    a = []
#    b = []
#    for i in range(1,10):
#        if i%2 == 0:
#            a.append(i)
#        else:
#            b.append(i)
#    print("even", a)
#    print("odd", b)
#if __name__ == '__main__':
#    main()

#def even(x):
#    return x%2 == 0
#def odd(x):
#    return x%2 == 1
#print(list(filter(even, [1,2,3,4,5,6,7,8,9,10])))
#print(list(filter(odd, [1,2,3,4,5,6,7,8,9,10])))



def main():
    result = {}
    keys = ['dolbal', 'sdhong', 'ianee', 'johnhaan']
    data = ['nm001','nm002','nm003','nm004']
    zipped = list(zip(keys, data)) 
    for k,v in zipped:
        result[k] = v
    print(result)
if __name__ ==  '__main__':
    main()