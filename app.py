# coding:utf-8
from flask import Flask, render_template, request, flash, redirect, url_for
from forms.login import *
from forms.finance import *
from src.database_connector import finance_reports
from flask_oidc import OpenIDConnect


# Setting up flask application
app = Flask(__name__)
app.debug = True
app.config.update({
        'SECRET_KEY': 'SomethingNotEntirelySecret',
        'OIDC_CLIENT_SECRETS': './client_secrets.json',
        'OIDC_ID_TOKEN_COOKIE_SECURE': False,
        'OIDC_SCOPES': ["openid", "profile", "email"],
        'OIDC_CALLBACK_ROUTE': '/authorization-code/callback'
    })
# Open ID Connect for Okta SSO
oidc = OpenIDConnect(app)

# a context processor which runs whenever anything runs on app.
# this gives us global access to the open id user object.
def user_context_processor():
    if oidc.user_loggedin:
        user = oidc.user_getinfo(["sub", "name", "email", "preferred_username"])
        print(user)
        # "scope": "email openid profile",
    else:
        user = None
    return {
        'user': user,
        'oidc': oidc
    }
app.context_processor(user_context_processor)

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
    print(oidc.credentials_store)
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
    if request.method == "POST":
        finance_reports( form.rep_name.data, form.start_date.data, form.end_date.data )
    return render_template('finance.html', title='gimme money', form=form)


if __name__ == "__main__":
    app.run(host="localhost", port=8081, debug=True);

   # {
   #   '00uinil2fky22vPfT0h7': '{"access_token": "eyJraWQiOiJsRnVVOFM0ZGRmazNPTlR2ZEFhZFl5SVRGbWV0aHZMSDVidFdKWGhCaEFrIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULlRwVkg2V0p1YUE0bW1mVUVYR3RNVDFvTGhMZ1hsU3RWdzJyTHNYUGJNVTgiLCJpc3MiOiJodHRwczovL2Rldi0zNzg4NDEub2t0YXByZXZpZXcuY29tL29hdXRoMi9kZWZhdWx0IiwiYXVkIjoiYXBpOi8vZGVmYXVsdCIsImlhdCI6MTU0NjAyOTI3MywiZXhwIjoxNTQ2MDMyODczLCJjaWQiOiIwb2FpbjRidXc2UHJhMUFSQTBoNyIsInVpZCI6IjAwdWluaWwyZmt5MjJ2UGZUMGg3Iiwic2NwIjpbImVtYWlsIiwib3BlbmlkIiwicHJvZmlsZSJdLCJzdWIiOiJtaWNoYWVsLnRlbmVyK3N1cGVybWFuQGFzcGNhLm9yZyJ9.VL-PkqQV-NX57RFTB5WvymBvh9h7b_7H05-42b-fgSvz3t4Bjrravsa-O9VH63-SQAH5ev2qx7IhBiwxtXieXDBGSJDt_c-DWEHHWEGPloFRhny_n4uLT50O4seLcA9NY1Tiz3M7XVyYcNMcU-CSzrn4iGKkRQ07KjcRsldTay4B8C-c3i5ZEeoFocywNk4BZuxO5iWwWcpL9ogtcGXNLyzyM1jsH1dmLP4VhXbedPnhY-W5YZ3mbZvd8al4PiNba0QZrdKXrf8CAwhFa_h84S_OTJrgzsE1b-4WoU35zEFmle6dFG4gGQQE7xnPjyysPxcW7r-Wm73GvES0aR_IDQ", "client_id": "0oain4buw6Pra1ARA0h7", "client_secret": "7gM7hODU8OgwCLQSGHBJpJABkSL9hHTxaBRs0-b6", "refresh_token": null, "token_expiry": "2018-12-28T21:34:34Z", "token_uri": "https://dev-378841.oktapreview.com/oauth2/default/v1/token", "user_agent": null, "revoke_uri": "https://oauth2.googleapis.com/revoke", "id_token": {"sub": "00uinil2fky22vPfT0h7", "name": "Super Man", "email": "michael.tener+superman@aspca.org", "ver": 1, "iss": "https://dev-378841.oktapreview.com/oauth2/default", "aud": "0oain4buw6Pra1ARA0h7", "iat": 1546029274, "exp": 1546032874, "jti": "ID.i56j2uixB6ngVZLSF86UZnAQjL6YniywmgGxDjXafpI", "amr": ["pwd"], "idp": "00oimwhdla2Bm9ifA0h7", "preferred_username": "michael.tener+superman@aspca.org", "auth_time": 1546027068, "at_hash": "Ik8yxX2xm60_lG3KRnya0A"}, "id_token_jwt": "eyJraWQiOiJsRnVVOFM0ZGRmazNPTlR2ZEFhZFl5SVRGbWV0aHZMSDVidFdKWGhCaEFrIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIwMHVpbmlsMmZreTIydlBmVDBoNyIsIm5hbWUiOiJTdXBlciBNYW4iLCJlbWFpbCI6Im1pY2hhZWwudGVuZXIrc3VwZXJtYW5AYXNwY2Eub3JnIiwidmVyIjoxLCJpc3MiOiJodHRwczovL2Rldi0zNzg4NDEub2t0YXByZXZpZXcuY29tL29hdXRoMi9kZWZhdWx0IiwiYXVkIjoiMG9haW40YnV3NlByYTFBUkEwaDciLCJpYXQiOjE1NDYwMjkyNzQsImV4cCI6MTU0NjAzMjg3NCwianRpIjoiSUQuaTU2ajJ1aXhCNm5nVlpMU0Y4NlVabkFRakw2WW5peXdtZ0d4RGpYYWZwSSIsImFtciI6WyJwd2QiXSwiaWRwIjoiMDBvaW13aGRsYTJCbTlpZkEwaDciLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJtaWNoYWVsLnRlbmVyK3N1cGVybWFuQGFzcGNhLm9yZyIsImF1dGhfdGltZSI6MTU0NjAyNzA2OCwiYXRfaGFzaCI6IklrOHl4WDJ4bTYwX2xHM0tSbnlhMEEifQ.JresD9n61kybqGQWZaDrxyAWrYK9Sf6jq763r9U1kKb9msCWjIIz2_f__Hg6mO-wBm3udVyfghNUwwo6IW8ZyzWX2n4PvhKdV5GT5pBfnyC_U3asJp9CbBqm9fbtj0ta5-7N5djyJUrQTw1DAr8k-3YO2MwGmxRciV6fPzHgMmN8EzvhUg-BHZlLE5K98VnaPp4npoM-FqO9-NYeIs95aLs7c_0DV97_9Z_EKOyD7b1vVIrBwqtKVbjFlTCZFfotLI97tcWJBlV9zNalnpmUNkwQV6jo4p0gZx8cMWSticcYKOcfbXNKdviEmDy-B6SClR-9DG2yVwS3Spzu9MoXgg", "token_response": {"access_token": "eyJraWQiOiJsRnVVOFM0ZGRmazNPTlR2ZEFhZFl5SVRGbWV0aHZMSDVidFdKWGhCaEFrIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULlRwVkg2V0p1YUE0bW1mVUVYR3RNVDFvTGhMZ1hsU3RWdzJyTHNYUGJNVTgiLCJpc3MiOiJodHRwczovL2Rldi0zNzg4NDEub2t0YXByZXZpZXcuY29tL29hdXRoMi9kZWZhdWx0IiwiYXVkIjoiYXBpOi8vZGVmYXVsdCIsImlhdCI6MTU0NjAyOTI3MywiZXhwIjoxNTQ2MDMyODczLCJjaWQiOiIwb2FpbjRidXc2UHJhMUFSQTBoNyIsInVpZCI6IjAwdWluaWwyZmt5MjJ2UGZUMGg3Iiwic2NwIjpbImVtYWlsIiwib3BlbmlkIiwicHJvZmlsZSJdLCJzdWIiOiJtaWNoYWVsLnRlbmVyK3N1cGVybWFuQGFzcGNhLm9yZyJ9.VL-PkqQV-NX57RFTB5WvymBvh9h7b_7H05-42b-fgSvz3t4Bjrravsa-O9VH63-SQAH5ev2qx7IhBiwxtXieXDBGSJDt_c-DWEHHWEGPloFRhny_n4uLT50O4seLcA9NY1Tiz3M7XVyYcNMcU-CSzrn4iGKkRQ07KjcRsldTay4B8C-c3i5ZEeoFocywNk4BZuxO5iWwWcpL9ogtcGXNLyzyM1jsH1dmLP4VhXbedPnhY-W5YZ3mbZvd8al4PiNba0QZrdKXrf8CAwhFa_h84S_OTJrgzsE1b-4WoU35zEFmle6dFG4gGQQE7xnPjyysPxcW7r-Wm73GvES0aR_IDQ", "token_type": "Bearer", "expires_in": 3600, "scope": "email openid profile", "id_token": "eyJraWQiOiJsRnVVOFM0ZGRmazNPTlR2ZEFhZFl5SVRGbWV0aHZMSDVidFdKWGhCaEFrIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIwMHVpbmlsMmZreTIydlBmVDBoNyIsIm5hbWUiOiJTdXBlciBNYW4iLCJlbWFpbCI6Im1pY2hhZWwudGVuZXIrc3VwZXJtYW5AYXNwY2Eub3JnIiwidmVyIjoxLCJpc3MiOiJodHRwczovL2Rldi0zNzg4NDEub2t0YXByZXZpZXcuY29tL29hdXRoMi9kZWZhdWx0IiwiYXVkIjoiMG9haW40YnV3NlByYTFBUkEwaDciLCJpYXQiOjE1NDYwMjkyNzQsImV4cCI6MTU0NjAzMjg3NCwianRpIjoiSUQuaTU2ajJ1aXhCNm5nVlpMU0Y4NlVabkFRakw2WW5peXdtZ0d4RGpYYWZwSSIsImFtciI6WyJwd2QiXSwiaWRwIjoiMDBvaW13aGRsYTJCbTlpZkEwaDciLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJtaWNoYWVsLnRlbmVyK3N1cGVybWFuQGFzcGNhLm9yZyIsImF1dGhfdGltZSI6MTU0NjAyNzA2OCwiYXRfaGFzaCI6IklrOHl4WDJ4bTYwX2xHM0tSbnlhMEEifQ.JresD9n61kybqGQWZaDrxyAWrYK9Sf6jq763r9U1kKb9msCWjIIz2_f__Hg6mO-wBm3udVyfghNUwwo6IW8ZyzWX2n4PvhKdV5GT5pBfnyC_U3asJp9CbBqm9fbtj0ta5-7N5djyJUrQTw1DAr8k-3YO2MwGmxRciV6fPzHgMmN8EzvhUg-BHZlLE5K98VnaPp4npoM-FqO9-NYeIs95aLs7c_0DV97_9Z_EKOyD7b1vVIrBwqtKVbjFlTCZFfotLI97tcWJBlV9zNalnpmUNkwQV6jo4p0gZx8cMWSticcYKOcfbXNKdviEmDy-B6SClR-9DG2yVwS3Spzu9MoXgg"}, "scopes": ["profile", "openid", "email"], "token_info_uri": "https://oauth2.googleapis.com/tokeninfo", "invalid": false, "_class": "OAuth2Credentials", "_module": "oauth2client.client"}'}
   # }