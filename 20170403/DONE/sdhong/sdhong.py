import sys
import pyping
from oslo_config import cfg
from oslo_log import log as oslo_logging

OPTS = [
    cfg.StrOpt("target_url",
                default="google.com"),
    cfg.StrOpt("target_protocol",
                 default="icmp"),
    cfg.StrOpt("log",
               default="./sdhong.log")
]

def register_options(cfg):
    cfg.register_opts(OPTS, "DEFAULT")
    cfg.register_cli_opts(OPTS, "DEFAULT")

CONF = cfg.CONF

def health_check(target):
    r = pyping.ping(target)
    return r

def main():
    register_options(CONF)
    oslo_logging.register_options(CONF)
    CONF(sys.argv[1:], default_config_files=['/etc/sdhong.conf'])
    oslo_logging.setup(CONF, 'DEFAULT')
    LOG = oslo_logging.getLogger(__name__)
    
    LOG.info("health_check: %s", CONF.DEFAUTL.target_url)


if __name__ == '__main__':
    main()
