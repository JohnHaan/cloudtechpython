try:
    from configparser import SafeConfigParser
except ImportError:
    # ConfigParser in python 2
    from ConfigParser import SafeConfigParser

config = SafeConfigParser()

config.add_section('Section1')

config.set('Section1', 'an_int', '15')
config.set('Section1', 'a_bool', 'true')
config.set('Section1', 'a_float', '3.1415')
config.set('Section1', 'baz', 'fun')
config.set('Section1', 'bar', 'Python')

with open('/projects/cloudtechpython/20170327/exercise_config/makesample.cfg', 'w') as configfile:
    config.write(configfile)