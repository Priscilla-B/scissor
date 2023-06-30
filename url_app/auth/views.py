from flask import request, Blueprint, flash, redirect, url_for, render_template
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from url_app.utils import db
from .models import User
from .forms import SignupForm


auth_views = Blueprint("auth_views", __name__)
        

@auth_views.route('/sign-up', methods=['GET', 'POST'])
def create_user():
    """
    Create a new user
    """
    form = SignupForm(request.form)
    if request.method == 'POST':
        
        if form.validate():
            
            hashed_password = generate_password_hash(form.password.data, 'sha256')
            new_user = User(
                first_name=form.first_name.data, 
                last_name=form.last_name.data, 
                email=form.email.data, 
                username=form.username.data, 
                password=hashed_password)
                
                    
            new_user.save()
            login_user(new_user)
            print(current_user, current_user)
            flash('Your account has been created successfully !')
            return redirect(url_for('url_views.home'))

    return render_template('auth/sign_up.html', form=form)
        
    
    

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
            flash('Incorrect username or password', category='error')
        
        if not check_password_hash(user.password, password):
            flash('Incorrect username or password.', category='error')
        else:
            is_logged_in = login_user(user, remember=True)
            if is_logged_in:
            
                flash('Logged in', category='success')
                return redirect(url_for('url_views.home'))
            else:
                flash('Incorrect username or password', category='error')

    return render_template('auth/login.html')

@auth_views.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out', category='success')
    return redirect(url_for('url_views.home'))



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
