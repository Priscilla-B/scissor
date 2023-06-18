from flask import request
from flask_jwt_extended import (jwt_required, get_jwt_identity)
from flask_restx import Namespace, Resource, marshal
from http import HTTPStatus

from api.auth.models import User

from .models import Url
from .serializers import shorten_url_serializer, shorten_url_response_serializer
from .mixins import UrlHelpersMixin

url_namespace = Namespace(
    'url',
    description='a namespace for url shortening logic')

shorten_url_model = url_namespace.model(
    'Url', shorten_url_serializer)
shorten_url_response_model = url_namespace.model(
    'Url', shorten_url_response_serializer
)

@url_namespace.route('/shorten_url')
class ShortenUrl(Resource, UrlHelpersMixin):

    @url_namespace.doc(description="Shorten a given url")
    @url_namespace.expect(shorten_url_model)
    @jwt_required()
    def post(self):
        """
        Save url information to database
        """
        data = request.get_json()

        user_id = get_jwt_identity()
        new_url = Url(
            target_url = data["target_url"],
            short_url = self.generate_short_url(5, request),
            user_id = user_id,
            user = User.get_by_id(user_id)

        )

        new_url.save()

        new_url_response = marshal(new_url, shorten_url_response_model)
        return new_url_response, HTTPStatus.CREATED