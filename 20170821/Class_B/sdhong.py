#
#import os
#
#def main():
#    raw_res = os.popen('ifconfig')
#    result = raw_res.read()
#    list = result.split()
#    print(list[6])
#if __name__ == '__main__':
#    main()

import os
def main():
    with open('sample.txt', 'r') as f:
        res_list = []
        res_dict = {}
        for line in f:
            line = line.strip()
            line = line.lower()
            line = line.replace(',', '')
            line = line.replace('.', '')
            line = line.split()
            res_list.extend(line)
            #res_list = list(set(res_list))
            #dict = {key: i for i, key in enumerate(res_list)}
            #list.count()

        print(res_list)
        for i in res_list:
            if i in res_dict.keys():
                res_dict[i] = res_dict[i] + 1
            else:
                res_dict[i] = 1
        print(res_dict)
            

if __name__ == '__main__':
    main()