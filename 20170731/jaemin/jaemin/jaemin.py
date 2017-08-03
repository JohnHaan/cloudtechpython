def add_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    print(target)

add_to(1)
add_to(2)
add_to(3)


class Myclass(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        
class Myclass(object):
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        
import pycurl

# As long as the file is opened in binary mode, both Python 2 and Python 3
# can write response body to it without decoding.
with open('out.html', 'wb') as f:
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://pycurl.io/')
    c.setopt(c.WRITEDATA, f)
    c.perform()
    c.close()

    