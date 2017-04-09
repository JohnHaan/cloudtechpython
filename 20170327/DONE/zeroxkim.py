# -*- coding:utf-8 -*-
import logging
import pyping
try:
    from configparser import SafeConfigParser
except ImportError:
    # ConfigParser in python 2
    from ConfigParser import SafeConfigParser


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
    
    
def listtest():
    #items = [1,5,2,1,9,1,5,10]
    #items = ['apple', 'banana', 'kiwi', 'banana', 'melon', 'apple']
    items = [{'x': 2, 'y': 3}, {'x': 1, 'y': 4}, {'x': 2, 'y': 3}, {'x': 2, 'y': 3}, {'x': 10, 'y': 15}]
    new_items = []
    
    for item in items:
        if item in new_items:
            pass
        else:
            new_items.append(item)
    
    print(new_items)
    
def main():
    #pingtest()
    
    listtest()
    
    
if __name__ == "__main__":
    main()
    