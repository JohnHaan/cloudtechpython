import sys
import logging
from oslo_config import cfg
from oslo_log import log as oslo_logging
from oslo_log import helpers as log_helpers
import pyping


OPTS = [
    cfg.StrOpt("target_url",
                default='www.naver.com'),
    cfg.StrOpt("target_protocol",
               default='http'),
    cfg.StrOpt("log_dir",
               default="/etc/son.log")
    
]

CONF = cfg.CONF
LOG = oslo_logging.getLogger(__name__)

def register_options(cfg):
    cfg.register_opts(OPTS, "logconf")
    cfg.register_cli_opts(OPTS, "logconf")

@log_helpers.log_method_call
def checkping(url):
    r = pyping.ping(url)
    LOG.info(url)
    if (r.ret_code == 0):
        LOG.info("success %s", r.destination)
    else:
        LOG.info("fail %s", r.destination)    
    

def main():
    register_options(CONF)
    oslo_logging.register_options(CONF)
    oslo_logging.set_defaults(log_dir='/projects/cloudtechpython/20170403/DONE/Masterson/son.log')
    CONF(sys.argv[1:], default_config_files=['problem.conf'] )
    oslo_logging.setup(CONF, 'demo')
    checkping(CONF.logconf.target_url)


if __name__ == '__main__':
    main()