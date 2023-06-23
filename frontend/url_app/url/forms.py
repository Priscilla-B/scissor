from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField, SelectMultipleField, ValidationError
from wtforms.validators import Length, InputRequired, EqualTo, Email


class UrlForm(FlaskForm):
    short_url = StringField(label='Short Url')
    email = EmailField(label='Email', validators=[Email(message='Invalid email address')])
    subject = StringField(label='Subject')
    message = TextAreaField(label='Body')
