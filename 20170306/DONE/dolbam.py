# -*- coding:utf-8 -*-
import locale
locale.setlocale(locale.LC_ALL, '')

def main():
    daum_v = 89000
    naver_v = 751000
    daum_n = 100
    naver_n = 20    
    calc(daum_v,naver_v,daum_n,naver_n)

def calc(daum_v,naver_v,daum_n,naver_n):
    tot = daum_v * daum_n + naver_v * naver_n
    tot_c = locale.format('%i', tot, 1)
    print("q1\n", "total =", tot_c)

if __name__ == '__main__':
    main()



#문제 2. 55페이지 아이디어 2

#문제 3. 56페이지 아이디어 4

#--------------
#q4
def main():
    h = dictcount('netmarblegames')
    print(h)

def dictcount(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
    
if __name__ == '__main__':
    main()
