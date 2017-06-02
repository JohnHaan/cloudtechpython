import sys

try:
    r = float(sys.argv[1]) / float(sys.argv[2])
    print("result: %s" % r)
except ZeroDivisionError:
    print("ZeroDivisionError")
except TypeError:
    print("TypeError")    
except Exception as e:
    print(e)
finally:
    print "divison is done." 
