from flask_wtf import Flaskform
from wtforms import StringField, EmailField. PasswordField
from wtforms.validators import DataRequired, Length, EqualTo,
                               Email, NumberRange, SubmitField


class register(Flaskform):
   username = StringField('username', validators=[Length(min=3, max=15),
                                                   DataRequired()])

   name = StringField('name', validators=[Length(min=3, max=20),
                                           DataRrquired()])

   email = EmailField('email', validators=[DataRequired(), Email()])

   pwd = StringField('password', validators=[DataRequired()])

   conf_pwd = PasswordField('re-enter Password',
                           validators=[DataRequired(), EqualTo(pwd)])

   phoneNo = StringField('phone number',
			   validators=[DataRequired(),
                           NumberRange(max=15)])

   signup = SubmitField('sign up')

class login(Flaskform):
    username = StringField('username', validators=[DataRequired()])

    pwd = PasswordField('password', validators=[DataRequired()])
