from flask_restx import Namespace, Resource, fields
from flask import request
from app.services.facade import HBnBFacade

api = Namespace('places', description='Place operations')
facade = HBnBFacade()

place_model = api.model('Place', 
    {
    'title': fields.String(required=True),
    'description': fields.String(),
    'price': fields.Float(required=True),
    'latitude': fields.Float(required=True),
    'longitude': fields.Float(required=True),
    'owner_id': fields.String(required=True),
    'amenities': fields.List(fields.String),
    })

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place created successfully')
    @api.response(400, 'Invalid data')
    def post(self):
        """Create a new place"""
     
        data = request.json
        place = facade.create_place(data)
        return ({
                "id": place.id,
                "title": place.title,
                "price": place.price,
                "latitude": place.latitude,
                "longitude": place.longitude
            }), 201

    @api.response(200, 'List of places')
    def get(self):
        """List all places"""
        places = facade.get_all_places()
        return ([
            {
                "id": p.id,
                "title": p.title,
                "price": p.price,
                "latitude": p.latitude,
                "longitude": p.longitude
            } for p in places
        ])

@api.route('/<string:place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get a specific place"""
        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404

        return ({
            "id": place.id,
            "title": place.title,
            "description": place.description,
            "price": place.price,
            "latitude": place.latitude,
            "longitude": place.longitude,
            "owner": {
                "id": place.owner.id,
                "first_name": place.owner.first_name,
                "last_name": place.owner.last_name,
                "email": place.owner.email
            },
            "amenities": [{"id": a.id, "name": a.name} for a in place.amenities]
        })

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    def put(self, place_id):
        """Update place info"""
        data = api.payload
        try:
            place = facade.update_place(place_id, data)
            return {"message": "Place updated successfully"}, 200
        except ValueError as e:
            return {"error": str(e)}, 404
        except Exception as e:
            return {"error": str(e)}, 400
