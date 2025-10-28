from flask_restx import Namespace, Resource, fields
from flask import request
<<<<<<< HEAD
from app.services.facade import HBnBFacade

api = Namespace('places', description='Place operations')
facade = HBnBFacade()
=======
from app.services import facade  # use shared facade instance

api = Namespace('places', description='Place operations')
>>>>>>> 8f49bfc437256fd86f415bc5296caa75e64161e1

amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

<<<<<<< HEAD
place_model = api.model('Place', 
    {
    'title': fields.String(required=True),
    'description': fields.String(),
    'price': fields.Float(required=True),
    'latitude': fields.Float(required=True),
    'longitude': fields.Float(required=True),
    'owner_id': fields.String(required=True),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
    })

=======
place_model = api.model('Place',
    {
        'title': fields.String(required=True),
        'description': fields.String(),
        'price': fields.Float(required=True),
        'latitude': fields.Float(required=True),
        'longitude': fields.Float(required=True),
        'owner_id': fields.String(required=True),
        'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
    })


>>>>>>> 8f49bfc437256fd86f415bc5296caa75e64161e1
@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place created successfully')
    @api.response(400, 'Invalid data')
    def post(self):
        """Create a new place"""
<<<<<<< HEAD
     
=======

>>>>>>> 8f49bfc437256fd86f415bc5296caa75e64161e1
        data = request.json
        owner = facade.get_user(data["owner_id"])
        if not owner:
            return {"Error": "invalid owner"}, 400

        place = facade.create_place(data)
        return ({
<<<<<<< HEAD
                "id": place.id,
                "title": place.title,
                "price": place.price,
                "latitude": place.latitude,
                "longitude": place.longitude

            }), 201
=======
                    "id": place.id,
                    "title": place.title,
                    "price": place.price,
                    "latitude": place.latitude,
                    "longitude": place.longitude
                }), 201
>>>>>>> 8f49bfc437256fd86f415bc5296caa75e64161e1

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

<<<<<<< HEAD
=======

>>>>>>> 8f49bfc437256fd86f415bc5296caa75e64161e1
@api.route('/<string:place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get a specific place"""
        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404
<<<<<<< HEAD
        
        amenities = []
=======
>>>>>>> 8f49bfc437256fd86f415bc5296caa75e64161e1

        amenities = []
        for amenity_id in place.amenities:
            amenity = facade.get_amenity(amenity_id)
            if amenity:
                amenities.append({
<<<<<<< HEAD
                "id": amenity.id,
                "name": amenity.name
=======
                    "id": amenity.id,
                    "name": amenity.name
>>>>>>> 8f49bfc437256fd86f415bc5296caa75e64161e1
                            })

        owner = facade.get_user(place.owner_id)
        return ({
            "id": place.id,
            "title": place.title,
            "description": place.description,
            "price": place.price,
            "latitude": place.latitude,
            "longitude": place.longitude,
<<<<<<< HEAD
            "owner":{
                "id":owner.id,
                "first name":owner.first_name,
                "last name":owner.last_name,
                "email":owner.email
                    },
            "amenities":amenities
=======
            "owner": {
                "id": owner.id,
                "first name": owner.first_name,
                "last name": owner.last_name,
                "email": owner.email
                    },
            "amenities": amenities
>>>>>>> 8f49bfc437256fd86f415bc5296caa75e64161e1
        })

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    def put(self, place_id):
        """Update place info"""
        data = api.payload

        place = facade.get_place(place_id)
        if not place:
<<<<<<< HEAD
            return{"Error": "Place not found"}, 404
        
=======
            return {"Error": "Place not found"}, 404

>>>>>>> 8f49bfc437256fd86f415bc5296caa75e64161e1
        owner = facade.get_user(data["owner_id"])
        if not owner:
            return {"Error": "Invalid owner"}, 400

        facade.update_place(place_id, data)

        return {"message": "Place updated successfully"}, 200
<<<<<<< HEAD
 
=======
>>>>>>> 8f49bfc437256fd86f415bc5296caa75e64161e1
