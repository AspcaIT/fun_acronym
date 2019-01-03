# coding:utf-8
from flask import Flask, render_template, request, redirect, url_for, session
from forms.login import *
from forms.finance import *
# from src.database_connector import finance_reports
from flask_oidc import OpenIDConnect
from src.tables.user import User
from src.database_connector import create_session


# Setting up flask application
app = Flask(__name__)
app.debug = True

# Copy the client_secrets.json.dist to client_secrets.json and refer to https://aspca.app.box.com/notes/372287586237
app.config.update({
        'SECRET_KEY': 'SomethingNotEntirelySecret',
        'OIDC_CLIENT_SECRETS': './client_secrets.json',
        'OIDC_ID_TOKEN_COOKIE_SECURE': False,
        'OIDC_SCOPES': ["openid", "profile", "email"],
        'OIDC_CALLBACK_ROUTE': '/authorization-code/callback'
    })
# Open ID Connect for Okta SSO
oidc = OpenIDConnect(app)

dude = "hi"

# a context processor which runs whenever anything runs on app.
# this gives us global access to the open id user object. Use user["name"] as the User ID
@app.context_processor
def user_context_processor():
    if oidc.user_loggedin:
        user = oidc.user_getinfo(["sub", "name", "email", "preferred_username"])
        print(oidc)
    else:
        user = None
    return {
        'user': user,
        'oidc': oidc
    }


# The default welcome page. This will be changed to the report list.
@app.route("/", methods=['GET', 'POST'])
@app.route("/<name>")
def welcome(name=None):
    form = WelcomeForm()
    # name = request.args.get('path')
    if request.method == "POST":
        name = form.fun_name.data
    return render_template("index.html", n=name, form=form)


# The @OIDC.require_login handles the OKTA authentication process for free.
# Todo Should also look up and set the app side user object
@app.route("/okta/login")
@oidc.require_login
def login():
    return redirect(url_for("finance_cust"))


# Used to log user out of application.
@app.route("/okta/logout")
def logout():
    oidc.logout()
    return redirect(url_for("welcome"))


@app.route('/finance', methods=['GET', 'POST'])
@oidc.require_login
def finance_cust():
    form = SqlForm()
    # if request.method == "POST":
        # finance_reports( form.rep_name.data, form.start_date.data, form.end_date.data )
    return render_template('finance.html', title='gimme money', form=form)


if __name__ == "__main__":
    app.run(host="localhost", port=8081, debug=True);