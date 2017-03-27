import example_configs as configs

LOG_DIR = configs.CONF.get('DEFAULT', 'log_dir')
LOG_FILE = configs.CONF.get('DEFAULT', 'log_file')

print(LOG_DIR)
print(LOG_FILE)