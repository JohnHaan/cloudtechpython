import logging
import configs


log_file = configs.CONF.get("DEFAULT", "log_file")
log_level = configs.CONF.get("DEFAULT", "log_level")

logging.basicConfig(stream=open(log_file, 'a'), level=log_level)