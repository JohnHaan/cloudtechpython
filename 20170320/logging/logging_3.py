# -*- coding:utf-8 -*-

import logging
logging.basicConfig(filename='./test.log',level=logging.DEBUG)

logging.info("=========================================")
logging.info("파일에다가 남겨봐요~")
logging.info("=========================================")
logging.debug("디버깅을 위한 메시지 로그")
logging.info("정보를 제공하기 위한 메시지 로그")
logging.warning("주의해야할 사항들")
logging.error("에러 발생!")
logging.critical("심각한 에러!!")