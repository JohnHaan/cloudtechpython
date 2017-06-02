from flask import Flask, request
import socket

hostname = socket.gethostname()

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/nova", methods=["GET"])
def nova():
    nova_port = 8774
    return "http://%s:%s" % ( hostname,nova_port)

@app.route("/glance", methods=["GET"])
def glance():
    glance_port = 9292
    return "http://%s:%s" % ( hostname,glance_port)

@app.route("/keystone", methods=["GET"])
def keystone():
    if (request.args.get('username') is not None):
        user_name = request.args['username']
    else:
        return 'invalid request'

    return "http://%s:5000/%s - Allowed User!" % ( hostname, user_name )


def main():
    app.run()
    #app.run(debug=True, host='0.0.0.0', port=5009)


if __name__ == "__main__":
    main()