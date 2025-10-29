from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})


@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        """Register a new amenity"""
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
        data = request.json

        if not data or 'name' not in data:
            api.abort(400, "Missing required field: name")
        try:
            amenity = facade.create_amenity({'name': data['name']})
            return amenity.to_dict(), 201
        except Exception as e:
            api.abort(400, str(e))

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        amenities = facade.get_all_amenities()
        return [a.to_dict() for a in amenities], 200


@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            api.abort(404, "Amenity with id{} not found".format(amenity_id))
        return amenity.to_dict(), 200

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def put(self, amenity_id):
        """Update an amenity's information"""
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
        
        data = request.json

        if not data or 'name' not in data:
            api.abort(400, "Missing required field: name")
        try:
            updated_amenity = facade.update_amenity(amenity_id, {'name': data['name']})
            if not updated_amenity:
                api.abort(
                    404,
                    "Amenity with the id {} not found".format(amenity_id))
            return updated_amenity.to_dict(), 200
        except Exception as e:
            api.abort(400, str(e))
