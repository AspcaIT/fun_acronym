# coding:utf-8
from flask import Flask, render_template
app = Flask(__name__)
app.debug=True

@app.route("/")
@app.route("/hi/<name>")
def hello(name):
    return render_template("index.html", n=name)

if __name__ == "__main__":
    app.run()