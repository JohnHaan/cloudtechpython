# -*- coding:utf-8 -*-

try:
    from configparser import SafeConfigParser
except ImportError:
    # ConfigParser in python 2
    from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
multi_confs = ['/projects/cloudtechpython/20170327/kiseok.ini',
               '/projects/cloudtechpython/20170327/kiseok2.ini']
parser.read(multi_confs)

"""
print(parser.get('bug_tracker', 'username'))
print(parser.get('bug_tracker', 'token'))
"""
for sn in parser.sections():
    print("# %s" % sn)
    for k, v in parser.items(sn):
        print("%s = %s" % (k, v))
