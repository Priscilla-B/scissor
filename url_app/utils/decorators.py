from ..auth.models import User

# Get the role of authenticated user
def get_user_role(id:int):
    user = User.query.filter_by(id=id).first()
    if user:
        return user.role
    else:
        return None
