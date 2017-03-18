from oslo_config import cfg
from oslo_log import log as logging
 
LOG = logging.getLogger(__name__)
CONF = cfg.CONF
DOMAIN = "test"

logging.register_options(CONF)
logging.setup(CONF, DOMAIN)

info = {"name": "kim", "city": "seoul"}
 
# Oslo Logging uses INFO as default
LOG.info("Logging name=> %(name)s, city=> %(city)s", info )
LOG.warning("Logging - %s", info)
LOG.error("Logging - %s", info.get("name"))
