from flask import request, Blueprint
from http import HTTPStatus

from .models import Analytics


analytics_views = Blueprint("analytics_views", __name__)

def save_url_analytics(request, url_code):
    ip = request.remote_addr
    print("**************ip address***********", ip)
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]

    new_data = Analytics(
        url_code = url_code,
        ip_address = ip

    )

    new_data.save()