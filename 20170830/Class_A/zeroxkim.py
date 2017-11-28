"""
def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)

search = grep("coroutine")
next(search)

search.send("I love you")
search.send("Don't you love me?")
search.send("I love coroutines instead!")
"""

"""
from functools import lru_cache

@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print([fib(n) for n in range(10)])

fib.cache_clear()
"""

"""
from functools import wraps

def memoize(function):
    memo = {}
    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper

@memoize
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(25))
"""

"""
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        print("Exception ha been handled")
        self.file_obj.close()
        return True

with File("zeroxkim.txt", "w") as opened_file:
    #opened_file.write("Hola!")
    opened_file.undefined_function("Hola!")
"""

"""
from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, "w")
    yield f
    f.close()

with open_file("zeroxkim.txt") as f:
    f.write("Hola!!")
"""

