# -*- coding:utf-8 -*-
'''
try:
    from configparser import SafeConfigParser
except ImportError:
    # ConfigParser in python 2
    from ConfigParser import SafeConfigParser
    
parser = SafeConfigParser()

#multi_conf = ['/projects/cloudtechpython/20170327/exercise_config/sonconf.ini',
#                '/projects/cloudtechpython/20170327/exercise_config/sonconf2.ini']

parser.read('/projects/cloudtechpython/20170327/exercise_config/sonconf.ini')

for sec_name in parser.sections():
    print("section %s",sec_name)
    print("options %s",parser.options(sec_name))
    for name, val in parser.items(sec_name):
        print('  %s = %s ' % (name, val))
    print
'''
import son_configs as configs

LOG_DIR = configs.CONF.get('DEFAULT','log_dir')
LOG_FILE = configs.CONF.get('DEFAULT','log_file')

print(LOG_DIR)
print(LOG_FILE)


