# coding:utf-8
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import Form StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


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
