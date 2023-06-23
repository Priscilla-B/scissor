import requests
import os
import json

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash


auth_views = Blueprint("auth_views", __name__)

@auth_views.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

    if os.environ.get('CONFIG_CHOSEN') == 'dev':
        endpoint = 'http://127.0.0.1:5000/api/auth/create_user'

    
    if request.method == 'POST':

        data = {
        "first_name":request.form.get('firstname'),
        "last_name":request.form.get('lastname'),
        "username":request.form.get('username'),
        "email":request.form.get('email'),
        "password":request.form.get('password')
        
        }

        response = requests.post(
            url=endpoint,
            data= data
        )
        
        if response.status_code == 201:
           
            flash('Your account has been created successfully !')
            return redirect(url_for('views.home'))
    
    return render_template('sign_up.html')


@auth_views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

     
    return render_template('login.html')


# @auth_views.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash('Logged out', category='success')
#     return redirect(url_for('views.home'))

