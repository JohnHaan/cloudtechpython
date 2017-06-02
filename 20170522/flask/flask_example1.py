from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
def main():
    app.run()
    #app.run(debug=True, host='0.0.0.0', port=5009)

if __name__ == "__main__":
    main()
