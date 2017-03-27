# -*- coding:utf-8 -*-

try:
    from configparser import SafeConfigParser
except ImportError:
    # ConfigParser in python 2
    from ConfigParser import SafeConfigParser

parser = SafeConfigParser()

multi_configs = ['/projects/cloudtechpython/20170327/exercise_config/sample1.ini',
                 '/projects/cloudtechpython/20170327/exercise_config/sample2.ini']

parser.read(multi_configs)

print(parser.get('bug_tracker', 'username'))
print(parser.get('bug_tracker', 'token'))