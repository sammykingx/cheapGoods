from flask_wtf import Flaskform
from wtforms import StringField, EmailField. PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo,
                               Email, number_range, SubmitField


class register(Flaskform):
   username = StringField('username', validators=[Length(min=3, max=15),
                                                   DataRequired()])

   name = StringField('name', validators=[Length(min=3, max=20),
                                           DataRrquired()])

   email = EmailField('email', validators=[DataRequired(), Email()])

   pwd = PasswordField('password', validators=[DataRequired()])

   conf_pwd = PasswordField('re-enter Password',
                           validators=[DataRequired(), EqualTo(pwd)])

   phoneNo = IntegerField('phone number',
			   validators=[DataRequired(), number_range('15')])

   signup = SubmitField('sign up')

class login(Flaskform):
    username = StringField('username', validators=[DataRequired()])

    pwd = PasswordField('password', validators=[DataRequired()])
