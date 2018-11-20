from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField

class SqlForm(FlaskForm):
    sql = TextAreaField('Sql', validators=[DataRequired()])
    from_date = DateField('Start Date', format='%Y-%m-%d', validators=[DataRequired()])
    to_date = DateField('End Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField("GIMME!")
