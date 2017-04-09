# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from datetime import datetime
import logging
import pyping
import requests

log_file = '/projects/cloudtechpython/20170320/DONE/sjhan.log'
log_level = 'DEBUG'
log_format = '[%(asctime)s: %(levelname)s/%(module)s] %(message)s'
logging.basicConfig(stream=open(log_file, 'a'), level=log_level,
                    format=log_format)
def main():
    # 1번 문제
    nowTime = datetime.now()
    str_now = nowTime.strftime('%Y-%m-%d %H:%M:%S')
    logging.debug('Start Healthcheck at (%s)', str_now)
    dest_url = 'daum.net'
    logging.debug('Desination URL : %s', dest_url)
    res = pyping.ping(dest_url)
    if not res.ret_code:
        logging.debug("Success")
    elif res.ret_code:
        logging.warning("Connection Failed")
    
    # 2번 문제
    URL = 'http://www.naver.com'
    res = requests.get(URL)
    soup = BeautifulSoup(res.text, 'lxml')
    datas = soup.find_all('a', attrs={'class': 'ah_a'})
    logging.debug('### 네이버 실시간 검색어 ###')
    for data in datas:
        rank = data.find('span', attrs={'class': 'ah_r'}).string
        name = data.find('span', attrs={'class': 'ah_k'}).string.strip()
        logging.debug('%s 위: %s', str(rank), name)

if __name__ == '__main__':
    main()