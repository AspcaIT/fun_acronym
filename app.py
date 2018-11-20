# coding:utf-8
from flask import Flask, render_template, request, flash, redirect
from forms.login import *
from forms.finance import *

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'puppies_and_kitties_are_super_awesome'


@app.route("/", methods=['GET', 'POST'])
@app.route("/<name>")
def welcome(name=None):
    form = WelcomeForm()
    # name = request.args.get('path')
    if request.method == "POST":
        name = form.fun_name.data
    return render_template("index.html", n=name, form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST":
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/finance', methods=['GET', 'POST'])
def finance_cust():
    form = SqlForm()
    return render_template('finance.html', title='gimme money', form=form)


sql_rep_dict = {
  "SNO Customer Report": "test/sno_cust_sql_table_test_v3.py",
  "APCC Customer Report": "test/apcc_cust_sql_table_test.py",
  "year": 1964
}


if __name__ == "__main__":
    app.run()