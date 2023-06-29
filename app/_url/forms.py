from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField, SelectMultipleField, ValidationError
from wtforms.validators import Length, InputRequired, EqualTo, Email


class ShortenUrlForm(FlaskForm):
    target_url = StringField(label='Target url')
    custom_domain = StringField(label='Custom domain')
    custom_short_text = TextAreaField(label='Custom text')
 