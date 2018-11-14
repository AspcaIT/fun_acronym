import flask
import wtforms

# App config.
DEBUG = True
app = flask.Flask( __name__ )
app.config.from_object( __name__ )
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm( wtforms.Form ):
    name = wtforms.StringField( 'Name:', validators=[wtforms.validators.DataRequired()] )


@app.route( "/", methods=['GET', 'POST'] )
def hello():
    form = ReusableForm( flask.request.form )

    print
    form.errors
    if flask.request.method == 'POST':
        name = flask.request.form['name']
        print
        name

        if form.validate():
            # Save the comment here.
            flask.flash( 'Hello ' + name )
        else:
            flask.flash( 'All the form fields are required. ' )

    return flask.render_template( 'hello.html', form=form )


if __name__ == "__main__":
    app.run()