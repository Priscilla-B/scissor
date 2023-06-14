from flask_restx import fields


shorten_url_serializer = {
        'target_url': fields.String(required=True, description='url you want to shorten')              
}

shorten_url_response_serializer = {
        'short_url': fields.String(required=True, description='short version of inputted url'),
        'target_url': fields.String(required=True, description='actual url short url redirects to')              
}


