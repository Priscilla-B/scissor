from flask import request, redirect
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
    'CreateUrl', shorten_url_serializer)
shorten_url_response_model = url_namespace.model(
    'GetUrl', shorten_url_response_serializer)

@url_namespace.route('/shorten_url')
class ShortenUrl(Resource, UrlHelpersMixin):

    @url_namespace.doc(description="Shorten a given url")
    @url_namespace.expect(shorten_url_model)
    @jwt_required()
    def post(self):
        """
        Generate a short url
        """
        data = request.get_json()

        user_id = get_jwt_identity()

        short_url = self.get_url_domain(request) + '/' + self.generate_short_text(request, 5)

        new_url = Url(
            target_url = data["target_url"],
            short_url = short_url,
            user_id = user_id,
            user = User.get_by_id(user_id)

        )

        new_url.save()

        new_url_response = marshal(new_url, shorten_url_response_model)
        return new_url_response, HTTPStatus.CREATED

@url_namespace.route('/urls')
class GetUrls(Resource):
    def get(self):
        """
        Get all urls
        """
        urls = Url.query.all()


@url_namespace.route('/<short_url>')
class RedirectToTarget(Resource):
    def get(self, short_url):
        """
        Redirect a given url to the destination url
        """

        url_obj = Url.query.filter_by(short_url=short_url).first()
        if url_obj:
            target_url = url_obj.target_url
            return {'redirect_url':target_url}
        else:
            return {'message': 'target url does not exist'}


       

        
        