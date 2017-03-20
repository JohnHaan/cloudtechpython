import pyping
server = pyping.ping('google.com') 
if server.ret_code == 0:
    print("Success")
else:
    print("Connection Failed")

