from flask import Flask
from flask_restx import Api
from app.Extensions import jwt, bcrypt, db
from config import DevelopmentConfig

from app.api.v1.places import api as places_ns
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.reviews import api as reviews_ns
from app.api.v1.auth import api as auth_ns


authorizations = {
    'Bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Entrer le token JWT comme : **Bearer <votre_token>**"
    }
}

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize SQLAlchemy with app
    db.init_app(app)

    # Set up bcrypt
    bcrypt.init_app(app)

    # Set up jwt
    jwt.init_app(app)

    # Set up API
    api = Api(
        app,
        version='1.0',
        title='HBnB API',
        description='HBnB Application API',
        doc='/api/v1/',
        authorizations=authorizations,
        security='Bearer'
    )

    # Register namespaces
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')
    api.add_namespace(auth_ns, path='/api/v1/auth')


    with app.app_context():
        from app.models.amenity import Amenity
        db.create_all()

    return app
