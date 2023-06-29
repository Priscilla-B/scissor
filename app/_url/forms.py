from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,ValidationError
from wtforms.validators import Length


class ShortenUrlForm(FlaskForm):
    target_url = StringField(label='Target url')
    custom_domain = StringField(label='Custom domain')
    custom_short_text = TextAreaField(label='Custom text')
 