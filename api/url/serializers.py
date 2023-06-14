from flask_restx import fields


shorten_url_serializer = {
        'target_url': fields.String(required=True, description='url you want to shorten')              
}


