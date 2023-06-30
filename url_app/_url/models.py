from sqlalchemy.sql import func

from url_app.utils import db
from url_app.utils.utils import ModelCreationMixin

class Url(db.Model, ModelCreationMixin):
    url_code = db.Column(db.String(5), primary_key=True)
    short_url = db.Column(db.String(30), nullable=False)
    target_url = db.Column(db.String(150), nullable=False)
    is_active = db.Column(db.Boolean(), default=True)
    user_id = db.Column(db.String(20), db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='user')