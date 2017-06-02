from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/info", methods=["GET"])
def test():

    if (request.args.get('name') is not None):
        nameinfo = request.args['name']
    else:
        return 'invalid request'

    return "your name is "+nameinfo

@app.route("/test", methods=["POST"])
def test():
    return "POST return"

def main():
    app.run()
    #app.run(debug=True, host='0.0.0.0', port=5009)

if __name__ == "__main__":
    main()