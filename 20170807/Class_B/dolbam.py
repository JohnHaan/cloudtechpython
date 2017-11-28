#def main():
#    z = []
#    x = []
#    for i in range(1,11):
#        r = i % 2
#        if r == 0 :
#            z.append(i) 
#        else:
#            x.append(i)
#
#    print('even', z)
#    print('odd', x)
#
#if __name__ == '__main__':
#    main()
#
#def even(x):
#    return x %2==0
#    
#def odd(y):
#    return y %2!=0
#    
#print('even', list(filter(even, [1,2,3,4,5,6,7,8,9,10])))
#print('even2', list(filter(even, range(1,11))))
#print('odd', list(filter(odd, [1,2,3,4,5,6,7,8,9,10])))
#print('odd2', list(filter(odd, range(1,11))))
#

#2. 김종원,이창재,홍성대,한승진 4명을 순서대로 사원번호를 부여하여 결과를 딕셔너리 형태로 출력하라.
#  - 사원번호 리스트 = [NM001, NM002, NM003, NM004]
#  - 결과 예시 : {김종원: NM001, ... }

def main():

    num=['NM001','NM002','NM003','NM004']
    name=['dolbam','ianlee','sdhong','sjhan']
    dic={}
    c=0
    for i in name :
        c=c+1
        dic[i] = num[c-1]

    print(dic)


if __name__ == '__main__':
    main()
