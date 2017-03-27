import requests
#import HTMLParser
from bs4 import BeautifulSoup
import urllib2
url = "http://www.naver.com"
soup = BeautifulSoup(urllib2.urlopen(url).read()) 

pkg_list=soup.findAll("span", "ell")

print(pkg_list)

