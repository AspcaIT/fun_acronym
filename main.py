# coding:utf-8
from flask import Flask, render_template, flash, redirect
from fun_acronym.forms.test_forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.debug = True


@app.route('/')
@app.route('/<name>')
def hello(name=None):

    return render_template('index.html', n=name)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash( 'Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data ) )
        #return redirect( '/' )
    return render_template('login.html', title='Sign In', form=form)


if __name__ == "__main__":
    app.run()