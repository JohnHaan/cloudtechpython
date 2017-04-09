# -*- coding:utf-8 -*-

try:
    from configparser import SafeConfigParser
except ImportError:
    # ConfigParser in python 2
    from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('/projects/cloudtechpython/20170327/sdhong.ini')

for section_name in parser.sections():
    print('Section: {}'.format(section_name))
    print('  Options: {}'.format(parser.options(section_name)))
    for name, value in parser.items(section_name):
        print('  %s = %s ' % (name, value))
    print