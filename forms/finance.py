from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DateField, SelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField


class SqlForm(FlaskForm):
    sql = TextAreaField('Sql', validators=[])
    rep_name = SelectField(
        'Select Report',
        choices=[('sno_cust_report.sql', 'SNO Customer Report'), ('apcc_cust_sql_table_test.sql', 'APCC Customer Report')])
    start_date = DateField('Start Date', format='%Y-%m-%d', validators=[])
    end_date = DateField('End Date', format='%Y-%m-%d', validators=[])
    submit = SubmitField("GIMME!")
