import logging
import pyping
import datetime

try:
    from configparser import SafeConfigParser
except:
    from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read(['/etc/ks.conf', 'ks.conf'])

logging.basicConfig(filename=parser.get("ping", "log_file"), level=logging.DEBUG)
LOG = logging.getLogger(__name__)

t = parser.get("ping", "target_url")
p = parser.get("ping", "target_protocol")
r = pyping.ping(t)
now = datetime.datetime.now()

if r.ret_code == 0:
    LOG.info("%s, %s ping(%s) success", now, p, t)
else:
    LOG.info("%s, %s ping(%s) fail", now, p, t)


def health_check(target):
    r = pyping.ping(target)
    return r
