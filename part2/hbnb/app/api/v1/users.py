from flask_restx import Namespace, Resource, fields
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services import facade

api = Namespace('users', description='User operations')

user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user')
})

user_update_model = api.model('UserUpdate', {
    'first_name': fields.String(description='First name of the user'),
    'last_name': fields.String(description='Last name of the user')
})


@api.route('/')
class UserList(Resource):
    @api.response(200, 'List of users retrieved successfully')
    def get(self):
        """Retrieve a list of all users"""
        users = facade.get_all_users()
        return [u.to_dict() for u in users], 200

    @api.expect(user_model)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Admin privileges required')
    @jwt_required()
    def post(self):
        """Create a new user (admin only)"""
        current_user_id = get_jwt_identity()
        claims = get_jwt()
        
        if not claims.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        user_data = api.payload
        email = user_data.get('email')

        if facade.get_user_by_email(email):
            return {'error': 'Email already registered'}, 400

        try:
            user = facade.create_user(user_data)
            return user.to_dict(), 201
        except ValueError as e:
            return {'error': str(e)}, 400


@api.route('/<string:user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {"message": "User not found"}, 404
        return user.to_dict(), 200

    @api.expect(user_update_model)
    @jwt_required()
    @api.response(200, 'User updated successfully')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Unauthorized action')
    @api.response(404, 'User not found')
    def put(self, user_id):
        """Update user info"""
        current_user_id = get_jwt_identity()
        claims = get_jwt()
        
        # Admin can modify anyone, regular users only themselves
        if not claims.get('is_admin') and str(current_user_id) != str(user_id):
            return {"error": "Unauthorized action"}, 403

        data = request.json or {}

        # Regular users cannot modify email/password
        if not claims.get('is_admin'):
            if not any(k in data for k in ['first_name', 'last_name']):
                return {"error": "No valid fields to update"}, 400

        # Admin can modify email
        if claims.get('is_admin') and 'email' in data:
            existing_user = facade.get_user_by_email(data['email'])
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email already in use'}, 400

        try:
            updated_user = facade.update_user(user_id, data)
            if not updated_user:
                return {"message": "User not found"}, 404
            return {"message": "User updated successfully"}, 200
        except ValueError as e:
            return {"message": str(e)}, 400