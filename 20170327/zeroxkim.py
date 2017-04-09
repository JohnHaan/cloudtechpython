# -*- coding:utf-8 -*-

import zeroxkim_config as configs

CONF = configs.init('zeroxkim')
LOG_DIR = CONF.get('DEFAULT', 'log_dir')
LOG_FILE = CONF.get('DEFAULT', 'log_file')

print(LOG_DIR)
print(LOG_FILE)
