from flask_restx import fields


shorten_url_serializer = {
        'target_url': fields.String(required=True, description='url you want to shorten'),
        'custom_domain': fields.String(required=True, description='custom domain to use in short url'),
        'custom_short_text': fields.String(required=True, description='custom short text to use in short url')           
}

shorten_url_response_serializer = {
        'short_url': fields.String(required=True, description='short version of inputted url'),
        'target_url': fields.String(required=True, description='actual url short url redirects to')              
}


