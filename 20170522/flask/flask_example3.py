from flask import Flask
app = Flask(__name__)

@app.route("/test", methods=["GET"])
def get_test():
    return "GET return"

@app.route("/test", methods=["POST"])
def post_test():
    return "POST return"

def main():
    app.run()
    #app.run(debug=True, host='0.0.0.0', port=5009)

if __name__ == "__main__":
    main()
    