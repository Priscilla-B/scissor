from sqlalchemy.sql import func

from api.utils import db
from api.utils.mixins import ModelCreationMixin




class Analytics(db.Model, ModelCreationMixin):
    __tablename__ = 'analytics'

    id = db.Column(db.Integer, primary_key=True)
    url_code = db.Column(db.String(5), db.ForeignKey('url.url_code'), nullable=False)
    url = db.relationship('Url', backref='url')
    ip_address = db.Column(db.String(150), nullable=True)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    
    
