from sqlalchemy.sql import func

from api.utils import db
from api.utils.mixins import ModelCreationMixin

class Url(db.Model, ModelCreationMixin):
    id = db.Column(db.Integer, primary_key=True)
    short_url = db.Column(db.String(10), nullable=False)
    target_url = db.Column(db.String(150), nullable=False)
    clicks = db.Column(db.Integer)
    is_active = db.Column(db.Boolean(), default=True)
    user = db.relationship()