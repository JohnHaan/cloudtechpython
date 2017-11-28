#import pickle
#
#with open("test2.txt",'wb') as f:
#    data = {1: 'python', 2: 'you need'}
#    pickle.dump(data, f)

#import glob
#print(glob.glob("/project/*"))

#import calendar
#
#print(calendar.prmonth(2015,12))    

#import webbrowser
#
#webbrowser.open_new("http://google.com")


#def main():
##    numbers = [1,2,3,4,5,6,7,8,9,10]
#    odd = list()
#    even = list()
#    
#    for number in range(1,11):
#        if number % 2:
##            print("odd")
#            odd.append(number)
#        else:
##            print("even")
#            even.append(number)
#            
#    print(odd)
#    print(even)
#        
#        
#
#if __name__ ==  '__main__':
#    main()
#
#def odd(x):
#    return x % 2 == 1
#def even(y):
#    return y % 2 == 0  
#    
#print(list(filter(odd, [1,2,3,4,5,6,7,8,9,10])))
#print(list(filter(even, [1,2,3,4,5,6,7,8,9,10])))
def main():

    nums = ['NM001','NM002','NM003','NM004']
    names = ['김종원','이창재','홍성대','한승진']

    result = {}

    for name in names:
        for num in nums:
    
            result[name] = num
        
    print(result)
        
if __name__ ==  '__main__':
    main()
