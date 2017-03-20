# import logging as symlog
# from oslo_log import log as logging
# from oslo_log import helpers as log_helpers

# LOG = logging.getLogger(__name__)
# symlog.basicConfig(level=symlog.DEBUG)

# #1 
# daum = 89000
# naver = 751000

# @log_helpers.log_method_call
# def get_price(sock_price, num):
# 	return sock_price * num

# @log_helpers.log_method_call
# def get_sum(*args):
# 	total = 0
# 	for arg in args:
# 		total += int(arg)
# 	return total

# total = get_sum( get_price(daum, 100), get_price(naver, 20))
# print("{:,}".format(total))

# 4
wc = {}
for i in "cloudtech":
	wc[i] = wc.get(i,0) + 1
print(wc)
