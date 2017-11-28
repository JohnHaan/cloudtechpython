

def remove_duplicate(l):
    res2_list=[]
    for i in l:
        if i in res2_list:
            pass
        else:
            res2_list.append(i)
    return res2_list

def wordscount(m):
    wordscount = {}
    for i in m:
        if i in wordscount.keys():
            e = wordscount.get(i)
            e = e + 1
            wordscount[i] = e
        else:
            wordscount[i] = 1

def main():
    with open('sample.txt','r') as f:
        res_list = []
        for read in f:
            read = read.strip()
            a = read.lower()
            b = a.replace(",","")
            c = b.replace(".","")
            d = c.split()
            res_list.extend(d)
        w = wordscount(res_list)
        print(w)

           
if __name__ ==  '__main__':
    main()
    
