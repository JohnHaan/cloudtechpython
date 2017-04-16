# -*- coding:utf-8 -*-
import pyping
import sys
from oslo_config import cfg
from oslo_log import log as oslo_logging
from oslo_log import helpers as log_helpers


OPTS = [
    cfg.StrOpt("target_url", default="google.com"),
    cfg.StrOpt("target_protocol", default="icmp"),
    cfg.StrOpt("log_file", default="./test.log")
]

CONF = cfg.CONF

LOG = oslo_logging.getLogger(__name__)


def register_options(cfg):
    cfg.register_opts(OPTS, "DEFAULT")
    cfg.register_cli_opts(OPTS, "DEFAULT")

    
@log_helpers.log_method_call
def pingtest(target):
    LOG.info('(in pingtest) %s' % CONF.DEFAULT.target_url)
    
    return pyping.ping(target)

    
def main():
    register_options(CONF)
    oslo_logging.register_options(CONF)
    CONF(sys.argv[1:], default_config_files=['/etc/zeroxkim.conf'])
    oslo_logging.setup(CONF, 'test')
    
    r = pingtest(CONF.DEFAULT.target_url)
    
    if r.ret_code == 0:
        result = 'Success'
    else:
        result = 'Failed'
    
    LOG.info('(in main) %s %s %s' % (CONF.DEFAULT.target_url, CONF.DEFAULT.target_protocol, result))
    
    
if __name__ == '__main__':
    main()
    