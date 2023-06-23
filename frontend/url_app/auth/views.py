from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import SignupForm


auth_views = Blueprint("auth_views", __name__)

@auth_views.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

    form = SignupForm(request.form)
    if request.method == 'POST':
        
        if form.validate():
           
            hashed_password = generate_password_hash(form.password.data, 'sha256')
           
            flash('Your account has been created successfully !')
            return redirect(url_for('views.home'))
    
    return render_template('sign_up.html', form=form)


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

