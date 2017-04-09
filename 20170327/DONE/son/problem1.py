import logging
import pyping
try:
    from configparser import SafeConfigParser
except ImportError:
    # ConfigParser in python 2
    from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('/etc/son.conf')
sec_name = 'dest_info'
target_url = ''
target_protocol = ''
log_file = ''
for name, val in parser.items(sec_name):
    print('  %s = %s ' % (name, val))
    if(name == 'target_url'):
        target_url = val
    if (name == 'target_protocol'):
        target_protocol = val
    if (name == 'log_file'):
        log_file = val

log_level = 'DEBUG'
log_format = '[%(asctime)s: %(levelname)s/%(module)s] %(message)s'
logging.basicConfig(stream=open(log_file, 'a'), level=log_level,
                    format=log_format)
r = pyping.ping(target_url)

if (r.ret_code == 0):
    logging.info("success %s", r.destination)
else:
    logging.info("fail %s", r.destination)