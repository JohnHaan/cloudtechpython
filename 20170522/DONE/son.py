from flask import Flask
from flask import request

app = Flask(__name__)
hostname = "192.168.0.11"

@app.route("/nova", methods=["GET"])
def novaAPI():
    endpoint = "http://"+hostname+":8774"
    return endpoint
@app.route("/glance", methods=["GET"])
def glanceAPI():
    endpoint = "http://"+hostname+":9292"
    return endpoint

@app.route("/keystone", methods=["GET"])
def keystoneAPI():
    endpoint=""
    if (request.args.get('username') is not None) :
        endpoint = endpoint = "http://"+hostname+":5000/"+request.args['username'] + " Allowed User!"
    return endpoint

def main():
    app.run(debug=True, host='0.0.0.0', port=5009)

if __name__ == "__main__":
    main()