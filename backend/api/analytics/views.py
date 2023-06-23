from flask import request
from flask_jwt_extended import (create_access_token, create_refresh_token, 
                                jwt_required, get_jwt_identity)
from flask_restx import Namespace, Resource, marshal
from http import HTTPStatus


from .models import Analytics

def save_url_analytics(request, url_code):
    ip = request.remote_addr
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]

    new_data = Analytics(
        url_code = url_code,
        ip_address = ip

    )

    new_data.save()