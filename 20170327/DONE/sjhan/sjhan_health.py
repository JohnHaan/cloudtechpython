# -*- coding:utf-8 -*-

from datetime import datetime
import pyping
import requests

from log import logging

LOG = logging.getLogger(__name__)


OPTS = [
    cfg.BoolOpt("enable",
                default=False),
    cfg.IntOpt("timeout",
                 min=3, max=60,
                 default=3),
    cfg.StrOpt("driver",
               default="my_driver")
]

def register_options(cfg):
    cfg.register_opts(OPTS, "myapp")
    cfg.register_cli_opts(OPTS, "myapp")

def main():
    # 1번 문제
    nowTime = datetime.now()
    str_now = nowTime.strftime('%Y-%m-%d %H:%M:%S')
    LOG.debug('Start Healthcheck at (%s)', str_now)
    dest_url = 'google.com'
    LOG.debug('Desination URL : %s', dest_url)
    res = pyping.ping(dest_url)
    if not res.ret_code:
        LOG.debug("Success")
    elif res.ret_code:
        LOG.warning("Connection Failed")

if __name__ == '__main__':
    main()