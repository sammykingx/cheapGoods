from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class register(FlaskForm):
   username = StringField('username', validators=[Length(min=3, max=15),
                                                   DataRequired()])

   name = StringField('name', validators=[Length(min=3, max=20),
                                           DataRequired()])

   email = EmailField('email', validators=[DataRequired(), Email()])

   pwd = PasswordField('password', validators=[DataRequired()])

   conf_pwd = PasswordField('re-enter Password', validators=[DataRequired()])

   phoneNo = StringField('Phone number',
			   validators=[DataRequired(),
                           Length(max=15)])

   signup = SubmitField('sign up')

class login(FlaskForm):
    username = StringField('username', validators=[DataRequired()])

    pwd = PasswordField('password', validators=[DataRequired()])

    login = SubmitField('login')
