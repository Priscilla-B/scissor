from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from http import HTTPStatus

from url_app.auth.models import User
from url_app.analytics.views import save_url_analytics

from .models import Url
from .forms import ShortenUrlForm
from .utils import generate_short_text, get_url_domain, url_is_valid

url_views = Blueprint("url_views", __name__)


@url_views.route('/', methods=['GET', 'POST'])
@url_views.route('/home', methods=['GET', 'POST'])
def home():
    form = request.form
    url = None
    if request.method == 'POST':

        if current_user.is_authenticated:
            user_id = current_user.get_id()
            user = User.get_by_id(user_id)
            
        else:
            user_id = None
            user = None

        target_url = form.get('long-url')

        if not url_is_valid(target_url):
            flash('Long url provided is not valid', category='error')
            request.form.target_url = target_url
            return render_template('_url/index.html', form = form)


        url_obj = Url.query.filter_by(
            target_url=target_url,
            user_id=user_id).first()
        if url_obj:
            url = url_obj
            flash('Returned your existing short url for provided long url ', category='success')

        else:
            
            url_code = generate_short_text(form, 5)
            short_url = get_url_domain(form, request)  + 'r/' + url_code

            url = Url(
                url_code = url_code,
                target_url = target_url,
                short_url = short_url,
                user_id = user_id,
                user = user

            )
            url.save()       

        return render_template('_url/index-url.html', url=url)

    else:
        return render_template('_url/index.html', form=form)


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

       

        