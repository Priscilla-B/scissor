from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_login import current_user, login_required

from .models import Analytics
from url_app._url.models import Url


analytics_views = Blueprint("analytics_views", __name__)

@analytics_views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    user_id = current_user.get_id()
    urls = Url.query.filter_by(user_id=user_id).all()
    return render_template('analytics/index.html', urls=urls)


def save_url_analytics(request, url_code):
    ip = request.remote_addr
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]

    new_data = Analytics(
        url_code = url_code,
        ip_address = ip

    )

    new_data.save()