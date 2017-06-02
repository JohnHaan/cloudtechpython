from flask import Flask
from flask import request
import socket

hostname = socket.gethostname()

app = Flask(__name__)

@app.route("/")
def endpoint():
    return "Please attach service name with url."
    
@app.route("/nova", methods=["GET"])
def novaEnd():
    return "http://%s:%s" % (hostname,8774)

@app.route("/glance", methods=["GET"])
def glanceEnd():
    return "http://%s:%s" % (hostname,9292)

@app.route("/keystone", methods=["GET"])
def keystoneEnd():
    if request.args.get('username'):
        user_name = request.args['username']

    return "http://%s:5000/%s - Allowed User!" % (hostname, username)
    
def main():
    app.run()

if __name__ == "__main__":
    main()