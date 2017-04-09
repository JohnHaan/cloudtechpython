# -*- coding:utf-8 -*-
import pyping
import sys
from oslo_config import cfg
from oslo_log import log as oslo_logging

CONF = cfg.CONF

OPTS = [
    cfg.StrOpt("target_url",
                default="google.com"),
    cfg.StrOpt("target_protocol",
                default="icmp"),
    cfg.StrOpt("log_dir",
                default="./log")
]

def register_options(cfg):
    cfg.register_opts(OPTS, "zeroxkim")
    cfg.register_cli_opts(OPTS, "zeroxkim")
    
    
#def pingtest(target):
    #r= pyping.ping(target)
    
    #return r
    
    
def main():
    register_options(CONF)
    oslo_logging.register_options(CONF)
    CONF(sys.argv[1:], default_config_files=['/etc/zeroxkim.conf'])
    oslo_logging.setup(CONF, 'zeroxkim')
    LOG = oslo_logging.getLogger(__name__)
    
    LOG.info("target_url: %s", CONF.zeroxkim.target_url)
    LOG.info("target_protocol: %s", CONF.zeroxkim.target_protocol)
    LOG.info("log_dir: %s", CONF.zeroxkim.log_dir)
    
    
if __name__ == '__main__':
    main()
    