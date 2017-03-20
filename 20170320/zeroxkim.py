# -*- coding:utf-8 -*-

import logging
import logging.handlers

# 로거 인스턴스를 만든다
logger = logging.getLogger('mylogger')

logger.setLevel(logging.DEBUG)

# 포매터를 만든다
fomatter = logging.Formatter('[%(asctime)s: %(levelname)s/%(module)s] %(message)s')

# 스트림과 파일로 로그를 출력하는 핸들러를 각각 만든다.
fileHandler = logging.FileHandler('./zeroxkim.log')

# 각 핸들러에 포매터를 지정한다.
fileHandler.setFormatter(fomatter)

# 로거 인스턴스에 스트림 핸들러 혹은 파일핸들러를 붙인다.
logger.addHandler(fileHandler)

logger.info("=========================================")
logger.info("파일에다가 남겨봐요~")
logger.info("=========================================")
logger.debug("디버깅을 위한 메시지 로그")
logger.info("정보를 제공하기 위한 메시지 로그")
logger.warning("주의해야할 사항들")
logger.error("에러 발생!")
logger.critical("심각한 에러!!")
