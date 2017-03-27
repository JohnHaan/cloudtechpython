# -*- coding:utf-8 -*-

try:
    from configparser import SafeConfigParser
except ImportError:
    # ConfigParser in python 2
    from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('/projects/cloudtechpython/20170327/exercise_config/sample1.ini')

print(parser.get('bug_tracker', 'url'))