from werkzeug.security import generate_password_hash
from .models import User


def save_user_obj(data):

    new_user = User(
            first_name = data.get('first_name'),
            last_name = data.get('last_name'),
            username = data.get('username'),
            email = data.get('email'),
            password = generate_password_hash(data.get('password'))
        )


    new_user.save()

    
    return new_user, 201
    

