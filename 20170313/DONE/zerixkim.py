import pyping
import time

# Q1
now = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
print("A1 : %s" % now)


# Q2
r = pyping.ping('10.105.180.25')

if r.ret_code == 0:
        print("A2 : Success")
else:
        print("A2 : Connection Failed")


# Q3
stock = [{'stock': 'naver', 'amount': 400}, {'stock': 'daum', 'amount': 300}, {'stock': 'naver', 'amount': 750}, {'stock': 'netmarle', 'amount': 340}, {'stock': 'daum', 'amount': 500}, {'stock': 'nexon', 'amount': 1000}, {'stock': 'daum', 'amount': 650}]

result = {}
daum_amount = 0
naver_amount = 0
nexon_amount = 0
netmarble_amount = 0

for a in stock:
        if a['stock'] == 'daum':
                daum_amount = daum_amount + a['amount']
        elif a['stock'] == 'naver':
                naver_amount = naver_amount + a['amount']
        elif a['stock'] == 'nexon':
                nexon_amount = nexon_amount + a['amount']
        else:
                netmarble_amount = netmarble_amount + a['amount']

        result['daum'] = daum_amount
        result['naver'] = naver_amount
        result['nexon'] = nexon_amount
        result['netmarble'] = netmarble_amount

print("A3 : %s" % result)