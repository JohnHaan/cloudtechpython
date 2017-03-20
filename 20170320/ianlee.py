# -*- coding:utf-8 -*-

import logging
import logging.handlers

logger = logging.getLogger('mylogger')

formatter = logging.Formatter('[%(asctime)s: %(levelname)s /%(module)s] %(message)s')

fileHandler = logging.FileHandler('./ianlee1.log')

fileHandler.setFormatter(formatter)

logger.addHandler(fileHandler)
# log_file = './ianlee.log'
log_level='DEBUG'
# log_format = '[%(asctime)s: %(levelname)s /%(module)s] %(message)s'
# logging.basicConfig(stream=open(log_file, 'a'), level=log_level, format=log_format)

logging.debug("디버깅을 위한 메세지 로그")
logging.info("정보를 제공하기 위한 메세지 로그")
logging.warning("주의해야할 사항들")
logging.error("에러발생")
logging.critical("심각한 에러!")