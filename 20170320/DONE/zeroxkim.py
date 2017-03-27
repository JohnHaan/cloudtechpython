# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import logging
import pyping
import requests

logFileName = "zeroxkim.log"
    
def pingtest():
    target = "google.com"
    result = ""
    
    r = pyping.ping(target)
    
    if r.ret_code == 0:
        result = "Success"
    else:
        result = "Failed"
    
    logger = logging.getLogger("zeroxkimlogger")
    logger.setLevel(logging.DEBUG)
    fomatter = logging.Formatter("[%(asctime)s: %(levelname)s/%(module)s] %(message)s")
    fileHandler = logging.FileHandler("./%s" % logFileName)
    fileHandler.setFormatter(fomatter)
    logger.addHandler(fileHandler)
    
    logger.info("%s %s" % (target, result))
    
    
def navertest():
    url = "http://www.naver.com"
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find_all("span",{"class":"ell"})
    
    logger = logging.getLogger("zeroxkimlogger")
    logger.setLevel(logging.DEBUG)
    fomatter = logging.Formatter("[%(asctime)s: %(levelname)s/%(module)s] %(message)s")
    fileHandler = logging.FileHandler("./%s" % logFileName)
    fileHandler.setFormatter(fomatter)
    logger.addHandler(fileHandler)
    
    logger.info("%s" % data)
    
    
def main():
    #pingtest()
    
    navertest()
    
    
if __name__ == "__main__":
    main()
