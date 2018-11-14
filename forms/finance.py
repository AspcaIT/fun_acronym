from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired


class SqlForm(FlaskForm):
    sql = TextAreaField('Sql', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    submit = SubmitField("GIMME!")
