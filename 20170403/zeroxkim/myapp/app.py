import sys
from oslo_config import cfg
from oslo_log import log as oslo_logging

OPTS = [
    cfg.BoolOpt("enable",
                default=False),
    cfg.FloatOpt("timeout",
                 min=3.05, max=60,
                 default=3.05),
    cfg.StrOpt("driver",
               default="my_driver")
]

def register_options(cfg):
    cfg.register_opts(OPTS, "myapp")
    cfg.register_cli_opts(OPTS, "myapp")

CONF = cfg.CONF

def main():
    register_options(CONF)
    oslo_logging.register_options(CONF)
    CONF(sys.argv[1:], default_config_files=['app.conf'])
    oslo_logging.setup(CONF, 'demo')
    LOG = oslo_logging.getLogger(__name__)
    
    #cfg.CONF.set_override("driver", "testtest", group="myapp")
    
    LOG.info("enable: %s", CONF.myapp.enable)
    LOG.info("timeout: %s", CONF.myapp.timeout)
    LOG.info("driver: %s", CONF.myapp.driver)

if __name__ == '__main__':
    main()
