import sys
from oslo_config import cfg
from oslo_log import log as oslo_logging
from oslo_log import helpers as log_helpers
import pyping
import datetime

OPTS = [
    cfg.StrOpt("target_url",
               default="google.com"),
    cfg.StrOpt("target_protocol",
               default="ping")
]

def register_options(cfg):
    cfg.register_opts(OPTS, "myapp")
    cfg.register_cli_opts(OPTS, "myapp")

CONF = cfg.CONF

@log_helpers.log_method_call
def health_check(target):
    r = pyping.ping(target)
    print(target)
    if r.ret_code == 0:
        return True
    else:
        return False

def main():
    register_options(CONF)
    oslo_logging.register_options(CONF)
    CONF(sys.argv[1:], default_config_files=['ks.conf'])
    oslo_logging.setup(CONF, 'demo')
    LOG = oslo_logging.getLogger(__name__)
    LOG.info(CONF.myapp.target_url)
    
    r = health_check(CONF.myapp.target_url)
    now = datetime.datetime.now()

    if r is True:
        LOG.info("%s ping success", CONF.myapp.target_url)
    else:
        LOG.info("%s ping fail", CONF.myapp.target_url)

if __name__ == '__main__':
    main()
