from sqlalchemy.sql import func

from url_app.utils import db
from url_app.utils.utils import ModelCreationMixin

class Url(db.Model, ModelCreationMixin):
    url_code = db.Column(db.String(7), primary_key=True)
    short_url = db.Column(db.String(150), nullable=False)
    target_url = db.Column(db.String(), nullable=False)
    is_active = db.Column(db.Boolean(), default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    user = db.relationship('User', backref='user')
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())