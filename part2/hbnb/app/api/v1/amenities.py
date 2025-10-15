from flask_restx import Namespace, Resource, fields
from app.services import facade

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
    def post(self):
        """Register a new amenity"""
        data = request.json
        if not data or 'name' not in data:
            api.abort(400, "Missing required field: name")
        try:
            amenity = facade.create_amenity(data['name'])
            return amenity, 201
        except Exception as e:
            api.abort(400, str(e))

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        amenities = facade.get.all_amenities()
        return amenities, 200


@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity_by_id(amenity_id)
        if not amenity:
            api.abort(404, "Amenity with id{} not found".format(amenity_id))
        return amenity, 200

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        data = request.json
        if not date or 'name' not in data:
            api.abort(400, "Missing required field: name")
        try:
            updated_amenity = facade.update_amenity(amenity_id, data['name'])
            if not updated_amenity:
                api.abort(
                    404,
                    "Amenity with the id {} not found".format(amenity_id))
            return updated_amenity, 200
        except Exception as e:
            api.abort(400, str(e))
