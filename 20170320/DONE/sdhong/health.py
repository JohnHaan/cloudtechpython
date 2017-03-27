# -*- coding:utf-8 -*-

import logging
import pyping

log_file = './health.log'
log_level = 'DEBUG'
log_format = '[%(asctime)s: %(levelname)s/%(module)s] %(message)s'
logging.basicConfig(stream=open(log_file, 'a'), level=log_level, format=log_format)
dest_url = 'google.com'
res_suc = 'success'
server = pyping.ping(dest_url)

if server.ret_code == 0:
    logging.debug('success')
    logging.debug(dest_url)
else:
    logging.warning('Connection Failed')
    logging.debug(dest_url)