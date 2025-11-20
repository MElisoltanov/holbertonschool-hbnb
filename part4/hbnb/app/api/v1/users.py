from flask_restx import Namespace, Resource, fields
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services import facade

api = Namespace('users', description='User operations')

# Modèles pour swagger
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

admin_update_model = api.model('AdminUserUpdate', {
    'first_name': fields.String(description='First name of the user'),
    'last_name': fields.String(description='Last name of the user'),
    'email': fields.String(description='Email of the user'),
    'password': fields.String(description='Password of the user')
})


# -----------------------
# Routes pour tous les utilisateurs
# -----------------------
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
    def post(self):
        """Create a new user (normal registration)"""
        data = request.json
        try:
            user = facade.create_user(data)
            return user.to_dict(), 201
        except ValueError as e:
            return {"message": str(e)}, 400


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
    @api.doc(security='BearerAuth')
    @jwt_required()
    @api.response(200, 'User updated successfully')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Unauthorized action')
    @api.response(404, 'User not found')
    def put(self, user_id):
        """Update own user info (first_name / last_name only)"""
        current_user = get_jwt_identity()
        if str(current_user) != str(user_id):
            return {"error": "Unauthorized action"}, 403

        data = request.json or {}
        if not any(k in data for k in ['first_name', 'last_name']):
            return {"error": "No valid fields to update"}, 400

        try:
            updated_user = facade.update_user(user_id, data)
        except ValueError as e:
            return {"message": str(e)}, 400

        if not updated_user:
            return {"message": "User not found"}, 404

        return {"message": "User updated successfully"}, 200


# -----------------------
# Routes admin
# -----------------------
@api.route('/admin/')
class AdminUserCreate(Resource):
    @jwt_required()
    @api.expect(user_model)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Admin privileges required')
    @api.doc(security='BearerAuth')
    def post(self):
        """Admin can create a new user"""
        claims = get_jwt()  # <-- FIXED
        if not claims.get("is_admin"):
            return {'error': 'Admin privileges required'}, 403

        user_data = request.json
        email = user_data.get('email')
        if facade.get_user_by_email(email):
            return {'error': 'Email already registered'}, 400

        try:
            user = facade.create_user(user_data)
            return user.to_dict(), 201
        except ValueError as e:
            return {"message": str(e)}, 400


@api.route('/admin/<string:user_id>')
class AdminUserModify(Resource):
    @jwt_required()
    @api.expect(admin_update_model)
    @api.response(200, 'User updated successfully')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Admin privileges required')
    @api.response(404, 'User not found')
    @api.doc(security='BearerAuth')
    def put(self, user_id):
        """Admin can update any user info, including email/password"""
        claims = get_jwt()  # <-- FIXED
        if not claims.get("is_admin"):
            return {'error': 'Admin privileges required'}, 403
        
        data = request.json or {}
        email = data.get('email')
        if email:
            existing_user = facade.get_user_by_email(email)
            if existing_user and str(existing_user.id) != str(user_id):
                return {'error': 'Email already in use'}, 400

        try:
            updated_user = facade.update_user(user_id, data)
        except ValueError as e:
            return {"message": str(e)}, 400

        if not updated_user:
            return {"message": "User not found"}, 404

        return {"message": "User updated successfully"}, 200
