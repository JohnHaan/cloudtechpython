# -*- coding:utf-8 -*-

from datetime import datetime
import pyping
import requests
import sys

from oslo_config import cfg
from oslo_log import helpers as log_helpers
from oslo_log import log as logging

LOG = logging.getLogger(__name__)

OPTS = [
    cfg.StrOpt("target_url",
                default="8.8.8.8"),
]

def register_options(cfg):
    cfg.register_opts(OPTS, "healthcheck")
    cfg.register_cli_opts(OPTS, "healthcheck")

CONF = cfg.CONF

@log_helpers.log_method_call
def health_check(target):
    return pyping.ping(target)

def main():
    register_options(CONF)
    logging.register_options(CONF)
    CONF(sys.argv[1:], default_config_files=['/etc/sjhan.conf'])
    logging.setup(CONF, 'demo')
    LOG = logging.getLogger(__name__)
    
    nowTime = datetime.now()
    str_now = nowTime.strftime('%Y-%m-%d %H:%M:%S')
    LOG.debug('Start Healthcheck at (%s)', str_now)
    LOG.debug('Desination URL : %s', CONF.healthcheck.target_url)
    res = health_check(CONF.healthcheck.target_url)
    if not res.ret_code:
        LOG.debug("Success")
    elif res.ret_code:
        LOG.warning("Connection Failed")

if __name__ == '__main__':
    main()