from collections import Counter

#def remove_duplicate(res_list):
#    res2_list = []
#    for i in res_list:
#        if i not in res2_list:
#            res2_list.append(i)
#    return res2_list
    
def main():
    with open('sample.txt', 'r') as f:
        res_list = []
        for line in f:
            line = line.strip()
            sline = line.lower()
            sline = sline.replace(',', '')
            sline = sline.replace('.', '')
            sline = sline.split()
            res_list.extend(sline)
#        res2_list = remove_duplicate(res_list)
        counts = Counter(res_list)
        print(counts)
        
            
#        print(res_list)
        
            
if __name__ == '__main__':
    main()
