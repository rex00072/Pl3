from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/")
def index():
    with open("index.html",'r') as file:
        return file.read()

if __name__ == '__main__':
    app.run(host="127.0.0.7",port="9999",use_reloader=True, debug=True)


