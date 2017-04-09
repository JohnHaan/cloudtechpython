# -*- coding:utf-8 -*-
from oslo_config import cfg
from oslo_log import log as logging
import pyping


def pingtest():
    parser = SafeConfigParser()
    parser.read('/etc/zeroxkim.conf')
    
    target = parser.get('DEFAULT', 'target_url')
    protocol = parser.get('DEFAULT', 'target_protocol')
    logFile = parser.get('DEFAULT', 'log_file')
    
    logger = logging.getLogger('zeroxkimlogger')
    logger.setLevel(logging.DEBUG)
    fomatter = logging.Formatter('[%(asctime)s: %(levelname)s/%(module)s] %(message)s')
    fileHandler = logging.FileHandler('%s' % logFile)
    fileHandler.setFormatter(fomatter)
    logger.addHandler(fileHandler)
    
    if protocol == 'udp':
        r = pyping.ping(target, udp = True)
    else:
        r = pyping.ping(target)
    
    if r.ret_code == 0:
        logger.info('%s %s %s' % (target, 'Success', protocol))
    else:
        logger.info('%s %s %s' % (target, 'Failed', protocol))
    
    
def main():
    pingtest()
    
    
if __name__ == "__main__":
    main()
    