import logging
import pyping
import datetime

logging.basicConfig(filename='kiseok_ping.log', level=logging.DEBUG)
LOG = logging.getLogger(__name__)

for t in ('google.com', 'facebook.com'):
    r = pyping.ping(t)
    now = datetime.datetime.now()
    if r.ret_code == 0:
        LOG.info("%s, %s ping success", now, t)
    else:
        LOG.info("%s, %s ping fail", now, t)
