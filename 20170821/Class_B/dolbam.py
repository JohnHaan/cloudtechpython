import os
import operator


#def main():
#    f = os.popen('ifconfig | grep \'inet addr\' | awk \'BEGIN {FS=":"} {print $2}\' | awk \'BEGIN {FS=" "} {print $1}\'')
#    ip=f.read()
#    print(ip)
#    
#if __name__=='__main__':
#    main()

def main():

    with open('sample.txt', 'r') as f:
        res_list=[]
        dol=[]
        dol2={}
 #       new_lst4=[]
        for list in f:
            line = list.strip()
            low = line.lower()
            new_lst = low.replace(',','')
            new_lst2=new_lst.replace('.','')
            new_lst3 = new_lst2.split()   
            res_list.extend(new_lst3)
          
        
            
        for i in res_list :
           # if i not in dol:
                dol.append(i)
        
        for o in dol :
            if o in dol2:
                dol2[o] += 1
            else : 
                dol2[o] = 1
                
        #print(len(dol))
        
        print(dol2)
        sorted_dict = sorted(dol2.items(), key=operator.itemgetter(1))
#            print("%s:'%d'" % (o, dol2[o]))
#        print(sorted_dict)

if __name__ == '__main__':
    main()


#import os
#
#def main():
#    raw_res = os.popen('ifconfig')
#    result = raw_res.read()
#    res_list = result.split()
#    for i in res_list:
#        if 'addr:' in i:
#            final_res = i.split(':')[1]
#            print(final_res)
#if __name__ == '__main__':
#    main()