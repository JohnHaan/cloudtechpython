import sys
from oslo_config import cfg
from oslo_log import log as logging

CONF = cfg.CONF

logging.register_options(CONF)
logging.setup(CONF, 'demo')
LOG = logging.getLogger(__name__)

LOG.info("Oslo info")
LOG.warning("Oslo war")
LOG.error("Oslo Error")
LOG.info("%(key)s, %(age)s", {"key":"hello", "age":10})