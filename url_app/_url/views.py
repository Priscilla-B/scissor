from urllib.parse import urlparse

from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_login import current_user, login_required
from http import HTTPStatus

from url_app.auth.models import User
from url_app.analytics.views import save_url_analytics

from .models import Url, db
from .forms import ShortenUrlForm
from .utils import generate_short_text, get_url_domain, url_is_valid, url_code_exists

url_views = Blueprint("url_views", __name__)


@url_views.route('/', methods=['GET', 'POST'])
@url_views.route('/home', methods=['GET', 'POST'])
def home():
    form = request.form
    url = None

    if current_user.is_authenticated:
        user_id = current_user.get_id()
        user = User.get_by_id(user_id)
    else:
        user_id = None
        user = None

    if request.method == 'POST':
        target_url = form.get('target_url')
        url_code = form.get('url_code') 

        
        if not url_is_valid(target_url):
            flash('Long url provided is not valid', category='error')
            return render_template('_url/index.html', form = form)
        
        if url_code != '' and url_code_exists(url_code):
            flash('Chosen custom text already exists for another url', category='error')
            return render_template('_url/index.html', form = request.form)


        url_obj = Url.query.filter_by(
            target_url=target_url,
            user_id=user_id).first()
        if url_obj:
            url = url_obj
            flash('Returned your existing short url for provided long url ', category='success')

        else:
            
            url_code = generate_short_text(form, 5)
            short_url = get_url_domain(form, request) + url_code

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
        form.domain = request.url_root
        return render_template('_url/index.html', form=form)


@url_views.route('/r/<url_code>/edit', methods=['GET', 'POST'])
@login_required
def edit_url(url_code):
    url = Url.query.filter_by(url_code=url_code).first()
    form = url

    if not url:
        flash("Url does not exist.", category='error')
        return render_template('_url/index.html', form = form)
    
    parsed_url = urlparse(url.short_url)
    form.domain = f'{parsed_url.scheme}://{parsed_url.netloc}'
    user_id = current_user.get_id()

    if user_id != url.user_id:
        flash('You do not have permission to edit this url.', category='error')
        
    else:
        if request.method == 'POST':
            form = request.form

            if not url_is_valid(form.get('target_url')):
                flash('Long url provided is not valid', category='error')
                return render_template('_url/index.html', form = form)

            if url_code_exists(form.get('url_code')):
                flash('Provided short text has been used for another url', category='error')

            else:
                url_code = generate_short_text(form, 5)
                short_url = get_url_domain(form, request) + url_code

                url.url_code = url_code
                url.target_url = form.get('target_url')
                url.short_url = short_url

                url.save() 
            flash('Url has been modified!', category='success')
            # session['url'] = url
            return redirect(url_for('url_views.url_view', url_code=url_code))
            # return render_template('_url/index-url.html', url=url)
   
        return render_template('_url/edit-url.html', form=form)

@url_views.route('/r/<url_code>/')  
@login_required
def url_view(url_code):
    url = Url.query.filter_by(url_code=url_code).first()
    user_id = current_user.get_id()
    if not url:
        flash("Url does not exist.", category='error')

    elif user_id != url.user_id:
        flash('You do not have permission to edit this url.', category='error')

    return render_template('_url/index-url.html', url=url)

@url_views.route('/r/<url_code>/delete')  
@login_required
def delete_url(url_code):
    url = Url.query.filter_by(url_code=url_code).first()
    user_id = current_user.get_id()
    if not url:
        flash("Url does not exist.", category='error')

    elif user_id != url.user_id:
        flash('You do not have permission to delete this url.', category='error')

    else:
        db.session.delete(url)
        db.session.commit()

    flash('Url has been deleted!', category='success')
    return redirect(url_for('url_views.home'))

    

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

       

        