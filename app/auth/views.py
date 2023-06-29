from flask import request, Blueprint
from flask_jwt_extended import (create_access_token, create_refresh_token, 
                                jwt_required, get_jwt_identity)
from werkzeug.security import generate_password_hash, check_password_hash

from app.utils import db
from .models import User
from .utils import save_user_obj


auth_views = Blueprint("auth_views", __name__)
        

@auth_views.route('/create_user')
    # @jwt_required()
def create_user(self):
    """
    Create a new user
    """
    data = request.get_json()

    create_user_response = save_user_obj(data)
    new_user = create_user_response[0]
    return new_user, create_user_response[1]
        
    
    

@auth_views.route('/login')
def post(self):
    """
    Login to get jwt token
    """
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = User.query.filter_by(email=email).first()

    if user is None:
        response = {"message": f"User with email {email} could not be found"}
        return response, 400
    
    if not check_password_hash(user.password, password):
        response =  {"message": "Password incorrect"}
        http_status = 400
    else:
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        response = {
            'access_token': access_token,
            'refresh_token': refresh_token
        }
        http_status = 200

    return response, http_status


@auth_views.route('/users')
@jwt_required()
def get_user(self):
    """
    Get a list of all users
    """

    users = User.query.all()

    return users


@auth_views.route('/users/<int:pk>')
@jwt_required()
def get_user(pk):
    """
    Get a user's details given their ID
    """

    user = User.get_by_id(pk)

    return user

@auth_views.route('/users/<int:pk>') 
@jwt_required()
def put(self, pk):
    """
    Update a user's details given their ID
    """

    user = User.get_by_id(pk)
    data = request.payload
    user_fields = [c.name for c in User.__table__.columns]

    for key, value in data.items():
        if key in user_fields:
            user[key] = value
        else:
            return {"msg":f"Could not update student with key {key}"}
    
    db.session.commit()
    

    return user

    
@auth_views.route('/users/<int:pk>') 
@jwt_required()
def delete(self, pk):
    """
    Delete a user's details given their ID
    """
    user = User.get_by_id(pk)

    user.delete()

    return {"message":f"User with id {pk} has been deleted"}


@auth_views.route('/refresh')
@jwt_required(refresh=True)
def refresh_tokem(self):
    """
    Get refresh token
    """
    username = get_jwt_identity()

    access_token = create_access_token(identity=username)


    return {'access_token': access_token}