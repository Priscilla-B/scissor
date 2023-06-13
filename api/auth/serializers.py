from flask_restx import fields


create_user_serializer = {
        'first_name': fields.String(required=True, description='first name of user'),
        'last_name': fields.String(required=True, description='last name of user'),
        'username': fields.String(required=True, description='public display name of user'),
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, 
                                  description='hash value of user password')                 
}



login_serializer = {
    'email':fields.String(required=True, description='user email address'),
    'password': fields.String(required=True, 
                                  description='user input of password')
}


get_user_serializer = {
        'id': fields.Integer(),
        'first_name': fields.String(required=True, description='first name of user'),
        'last_name': fields.String(required=True, description='last name of user'),
        'username': fields.String(required=True, description='public display name of user')       
}

