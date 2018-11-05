# coding:utf-8
from flask import Flask, render_template
from forms.test_forms import LoginForm
app = Flask(__name__)
app.debug = True


@app.route("/")
@app.route("/<name>")
def hello(name=None):
    return render_template("index.html", n=name)


@app.route('/login')
def login():
    form = ()
    return render_template('login.html', title='Sign In', form=form)


if __name__ == "__main__":
    app.run()