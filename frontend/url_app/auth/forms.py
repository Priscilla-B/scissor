from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField, SelectMultipleField, ValidationError
from wtforms.validators import Length, InputRequired, EqualTo, Email

class SignupForm(FlaskForm):
    first_name = StringField(label='First name')
    last_name = StringField(label='Last name')
    username = StringField(
        label='Username',
        validators=[Length(min=3, max=25, 
        message='Username length must be between %(min)d and %(max)d characters')]
        )

    email = EmailField(label='Email')

    password = PasswordField(label='New Password', 
        validators=
        [InputRequired(), 
        Length(min=8, message='Password should be 8 or more characters long'),
        EqualTo('confirm', message='Passwords do not match!')])
    confirm  = PasswordField(label='Repeat Password')

   



