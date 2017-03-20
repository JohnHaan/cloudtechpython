def translater(arr):
    ndic = {}
    for i in arr:
        if (ndic.get(i['stock']) is None):
            ndic[i['stock']] = i['amount']
        else:
            ndic[i['stock']] += i['amount']
    print (ndic)

if __name__ == '__main__':
    # arr = [{'stock':'naver', 'amount':400}, {'stock':'daum', 'amount':300}, {'stock':'naver', 'amount': 750}]
	arr = [{'stock': 'naver', 'amount': 400}, {'stock': 'daum', 'amount': 300}, {'stock': 'naver', 'amount': 750}, {'stock': 'netmarble', 'amount': 340}, {'stock': 'daum', 'amount': 500}, {'stock': 'nexon', 'amount': 1000}, {'stock': 'daum', 'amount': 650}]
	translater(arr)