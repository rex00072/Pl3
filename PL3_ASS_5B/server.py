from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/p1")
def index():
    with open("blockchain.html",'r',encoding='utf-8') as file:
        return file.read()

@app.route("/p2")
def P2():
    with open("Code.html",'r',encoding='utf-8') as file:
        return file.read()
@app.route("/p3")
def P3():
    with open("quotes.html",'r',encoding='utf-8') as file:
        return file.read()

if __name__ == '__main__':
    app.run(host="127.0.0.7",port="9999",use_reloader=True, debug=True)


