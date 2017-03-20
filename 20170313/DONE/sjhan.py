# -*- coding:utf-8 -*-

from datetime import datetime
import pyping

def main():
    # 1번 문제
    nowTime = datetime.now()
    strNow = nowTime.strftime('%Y-%m-%d %H:%M:%S')
    print(strNow)

    # 2번 문제
    dest_url = 'google.com'
    res = pyping.ping(dest_url)
    if not res.ret_code:
        print("Success")
    elif res.ret_code:
        print("Connection Failed")

    #  3번 문제
    q_list = [{'stock': 'naver', 'amount': 400}, {'stock': 'daum', 'amount': 300}, {'stock': 'naver', 'amount': 750}]
#    q_list = [{'stock': 'naver', 'amount': 400}, {'stock': 'daum', 'amount': 300}, {'stock': 'naver', 'amount': 750}, {'stock': 'netmarble', 'amount': 340}, {'stock': 'daum', 'amount': 500}, {'stock': 'nexon', 'amount': 1000}, {'stock': 'daum', 'amount': 650}]
    res_dict = {}
    for stock_dict in q_list:
        stock = stock_dict['stock']
        amount = stock_dict['amount']
        if stock not in res_dict.keys():
            res_dict[stock] = amount
        elif stock in res_dict.keys():
            res_dict[stock] += amount
        else:
            print("Unexpected Error!")
    print(res_dict)

if __name__ == '__main__':
    main()