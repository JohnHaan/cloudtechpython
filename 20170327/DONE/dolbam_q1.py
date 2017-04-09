import dolbam_q1_configs as configs
import logging
import pyping
import datetime

log_url = configs.CONF.get('DEFAULT', 'url')
log_protocol = configs.CONF.get('DEFAULT', 'protocol')

print(log_url, log_protocol)
logging.basicConfig(filename='dolbam_health.log', level=logging.DEBUG)
LOG = logging.getLogger(__name__)

#for t in log_url:
#    r = pyping.ping(t)
#    now = datetime.datetime.now()
#    if r.ret_code == 0:
#        LOG.info("%s, %s ,%s success", now, t, log_protocol)
#    else:
#        LOG.info("%s, %s, %s fail", now, t, log_protocol)
r = pyping.ping(log_url)
now = datetime.datetime.now()
if r.ret_code == 0:
    LOG.info("%s, %s ,%s success", now, log_url, log_protocol)
else:
    LOG.info("%s, %s, %s fail", now, log_url, log_protocol)