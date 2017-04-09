import kiseok_configs as conf

LOG_DIR = conf.CONF.get("DEFAULT", "log_dir")
LOG_FILE = conf.CONF.get("DEFAULT", "log_file")
print(LOG_DIR)
print(LOG_FILE)
