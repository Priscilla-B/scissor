from sqlalchemy.sql import func
from flask_login import UserMixin

from url_app.utils import db
from url_app.utils.utils import ModelCreationMixin




class User(db.Model, ModelCreationMixin, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    
    def __repr__(self):
        return f'{self.username}'
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

