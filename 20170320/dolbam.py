# -*- coding:utf-8 -*-

import logging

# log_file = './test.log'
# log_level = 'DEBUG'
# log_format = '[%(asctime)s: %(levelname)s/%(module)s] %(message)s'
# print ("time : %(localtime)s, %(localzone)s", localtime=localtime, localzone=localzone)
#logging.basicConfig(stream=open(log_file, 'a'), level=log_level,
#                    format=log_format)
import logging.handlers

# 로거 인스턴스를 만든다
logger = logging.getLogger('mylogger')

#logger.setLevel(logging.DEBUG)

# 포매터를 만든다
fomatter = logging.Formatter('[%(asctime)s: %(levelname)s/%(module)s] %(message)s')

# 스트림과 파일로 로그를 출력하는 핸들러를 각각 만든다.
fileHandler = logging.FileHandler('./dolbam.log')

# 각 핸들러에 포매터를 지정한다.
fileHandler.setFormatter(fomatter)

# 로거 인스턴스에 스트림 핸들러 혹은 파일핸들러를 붙인다.
logger.addHandler(fileHandler)
logger.setLevel('DEBUG')


logging.info("=========================================")
logging.info("파일에다가 남겨봐요~")
logging.info("=========================================")
logging.debug("디버깅을 위한 메시지 로그")
logging.info("정보를 제공하기 위한 메시지 로그")
logging.warning("주의해야할 사항들")
logging.error("에러 발생!")
logging.critical("심각한 에러!!")

