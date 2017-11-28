from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    yield f
    f.close()

with open_file('demo.txt') as opened_file:
    opened_file.write("hello")
