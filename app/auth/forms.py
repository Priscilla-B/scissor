from flask_wtf import FlaskForm
from .models import User
from wtforms import (
    StringField,PasswordField, 
    EmailField, ValidationError)
from wtforms.validators import Length, InputRequired, EqualTo, Email

class SignupForm(FlaskForm):
    first_name = StringField(label='First name')
    last_name = StringField(label='Last name')
    username = StringField(
        label='Username',
        validators=[Length(min=3, max=25, 
        message='Username length must be between %(min)d and %(max)d characters')]
        )

    email = EmailField(label='Email', validators=[Email(message='Invalid email address')])

    password = PasswordField(label='New Password', 
        validators=
        [InputRequired(), 
        Length(min=8, message='Password should be 8 or more characters long'),
        EqualTo('confirm', message='Passwords do not match!')])
    confirm  = PasswordField(label='Repeat Password')

    def validate_email(self, email):
        email_exists = User.query.filter_by(email=email.data).first()
        if email_exists:
            raise ValidationError('Email already exists.')

    def validate_username(self, username):
        username_exists = User.query.filter_by(username=username.data).first()
        if username_exists:
            raise ValidationError('Username is taken !')


