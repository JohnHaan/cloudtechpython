import logging
import pyping

log_file = './test.log'
log_level = 'DEBUG'
log_format = '[%(asctime)s: %(levelname)s/%(module)s] %(message)s'
logging.basicConfig(stream=open(log_file, 'a'), level=log_level,
                    format=log_format)

r = pyping.ping('google.com')

if (r.ret_code == 0):
    logging.info("success %s", r.destination)
else:
    logging.info("fail %s", r.destination)
