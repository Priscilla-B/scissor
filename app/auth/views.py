from flask import request, Blueprint, flash, redirect, url_for, render_template
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from app.utils import db
from .models import User
from .utils import save_user_obj


auth_views = Blueprint("auth_views", __name__)
        

@auth_views.route('/create_user')
    # @jwt_required()
def create_user():
    """
    Create a new user
    """
    data = request.get_json()

    create_user_response = save_user_obj(data)
    new_user = create_user_response[0]
    return new_user, create_user_response[1]
        
    
    

@auth_views.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login to get jwt token
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user is None:
            flash('User or email doesn\'t exist', category='error')
        
        if not check_password_hash(user.password, password):
            flash('Password is incorrect', category='error')
        else:
            flash('Logged in', category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.home'))

    return render_template('login.html')


@auth_views.route('/users')
def get_users():
    """
    Get a list of all users
    """

    users = User.query.all()

    return users


@auth_views.route('/users/<int:pk>')
def get_user(pk):
    """
    Get a user's details given their ID
    """

    user = User.get_by_id(pk)

    return user

@auth_views.route('/users/<int:pk>') 
def update_user(pk):
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
def delete_user(pk):
    """
    Delete a user's details given their ID
    """
    user = User.get_by_id(pk)

    user.delete()

    return {"message":f"User with id {pk} has been deleted"}
