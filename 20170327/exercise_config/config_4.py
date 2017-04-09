import example_configs as configs

CONF = configs.init('example')

LOG_DIR = CONF.get('DEFAULT', 'log_dir')
LOG_FILE = CONF.get('DEFAULT', 'log_file')

print(LOG_DIR)
print(LOG_FILE)