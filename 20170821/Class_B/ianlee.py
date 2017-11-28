#1. ifconfig 명령어를 통해 얻은 정보에서 서버의 ip 주소만 출력하는 프로그램을 만드시오.
#
#2. 제시된 sample.txt 파일에서 아래의 결과를 출력하는 프로그램을 만드시오.
#  - 기사에 사용된 총 단어의 수를 구하시오.
#  - 기사에 사용된 각 단어의 수를 dictionary 형태로 출력하시오.
#    예> {and:3, Docker:2...}
#  - 
#  
#  힌트 :
#   - 문자열 내장함수 : split(), count(), replace(), strip(), lower()
#   - 리스트 내장함수 : extend()

#import os
#
#def main():
#    a = os.popen("ifconfig")
#    
#    a = a.read()
#    #print(a)
#    b = a.split()
#    for i in b
#        if 'addr:' in i
#            
#    print(b)
#    #print(c)
#    #print(type(a))
#
#
#if __name__ ==  '__main__':
#    main()

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