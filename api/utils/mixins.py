
from . import db

class ModelCreationMixin(object):
    """
    Custom methods and helpers that are common across models.
    Defines getters, setters, save, delete, dict converstion and get by id methods.
    """

    def __getitem__(self, key):
        """
        To enable item assignments such as user["name"]
        instead of user.name
        """
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        """
        To enable item re-assignments such as user["name"] = "new name"
        instead of user.name = "new name"
        """
        return setattr(self, key, value)
    
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

