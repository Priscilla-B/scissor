from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError
from wtforms.validators import Length


class ShortenUrlForm(FlaskForm):
    target_url = StringField(label='Target url')
    custom_domain = StringField(label='Custom domain')
    custom_short_text = StringField(label='Custom text')
 