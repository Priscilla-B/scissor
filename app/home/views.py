from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required


home_views = Blueprint("views", __name__)

@home_views.route('/')
@home_views.route('/home')
def home():

    return render_template('index.html')