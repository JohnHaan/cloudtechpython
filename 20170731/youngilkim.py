#!/projects/cloudtechpython/20170731/ks/proj/bin/python

import pycurl

c = pycurl.Curl()
c.setopt(pycurl.URL, "http://www.python.org/")
c.perform()
print ( c.getinfo(pycurl.HTTP_CODE), c.getinfo(pycurl.EFFECTIVE_URL) )