from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from http import HTTPStatus

from app.auth.models import User
from app.analytics.views import save_url_analytics

from .models import Url
from .utils import generate_short_text, get_url_domain

url_views = Blueprint("url_views", __name__)


@url_views.route('/')
@url_views.route('/home')
def home():

    return render_template('_url/index.html')


@url_views.route('/shorten_url')
def shorten_url(self):
    """
    Generate a short url
    """
    data = request.get_json()

    user_id = current_user.get_id()

    url_obj = Url.query.filter_by(
        target_url=data['target_url'],
        user_id=user_id).first()
    if url_obj:
        # return marshal(url_obj, shorten_url_response_model)
        pass

    url_code = generate_short_text(request, 5)
    short_url = get_url_domain(request)  + 'r/' + url_code

    new_url = Url(
        url_code = url_code,
        target_url = data["target_url"],
        short_url = short_url,
        user_id = user_id,
        user = User.get_by_id(user_id)

    )

    new_url.save()

    # new_url_response = marshal(new_url, shorten_url_response_model)
    return new_url, HTTPStatus.CREATED

@url_views.route('/urls')
@login_required
def get_urls():
    """
    Get all urls
    """
    user_id = current_user.get_id()
    urls = Url.query.filter_by(user_id=user_id).all()

    return urls
        


@url_views.route('/r/<url_code>')
def redirect_to_target(url_code):
    """
    Redirect a given url to the destination url
    """
    save_url_analytics(request, url_code)
    
    url_obj = Url.query.filter_by(url_code=url_code).first().target_url

    return redirect(url_obj)

       

        
        