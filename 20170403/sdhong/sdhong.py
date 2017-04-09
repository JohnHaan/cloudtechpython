import sys
from oslo_config import cfg
from oslo_log import log as logging

CONF = cfg.CONF

logging.register_options(CONF)
logging.setup(CONF, 'demo')
LOG = logging.getLogger(__name__)

LOG.info("%(key)s, %(age)d", {"key":"hello", "age" : 10})
LOG.warning("Oslo Warning Logging")
LOG.error("Oslo Error Logging")
