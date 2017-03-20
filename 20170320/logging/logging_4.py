# -*- coding:utf-8 -*-

import logging

log_file = './test.log'
log_level = 'DEBUG'
log_format = '[%(asctime)s: %(levelname)s/%(module)s] %(message)s'
# print ("time : %(localtime)s, %(localzone)s", localtime=localtime, localzone=localzone)
logging.basicConfig(stream=open(log_file, 'a'), level=log_level,
                    format=log_format)

logging.info("=========================================")
logging.info("파일에다가 남겨봐요~")
logging.info("=========================================")
logging.debug("디버깅을 위한 메시지 로그")
logging.info("정보를 제공하기 위한 메시지 로그")
logging.warning("주의해야할 사항들")
logging.error("에러 발생!")
logging.critical("심각한 에러!!")

