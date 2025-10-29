from flask import Flask
from flask_restx import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager  
from app.api.v1.places import api as places_ns
from app.api.v1/users import api as users_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.reviews import api as reviews_ns

# Création de l'instance Bcrypt
bcrypt = Bcrypt()
# Création de l'instance JWTManager
jwt = JWTManager()

def create_app(config_class="config.DevelopmentConfig"):
    # Création de l'application Flask
    app = Flask(__name__)

    # Chargement de la configuration
    app.config.from_object(config_class)

    # Initialisation de Bcrypt avec l'app
    bcrypt.init_app(app)
    # Initialisation de JWT avec l'app
    jwt.init_app(app)

    # Création de l'API RESTX
    api = Api(
        app,
        version='1.0',
        title='HBnB API',
        description='HBnB Application API',
        doc='/api/v1/'
    )

    # Ajout des namespaces
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(places_ns, path="/api/v1/places")
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')

    from app.api.v1.auth import api as auth_ns
    api.add_namespace(auth_ns, path='/api/v1/auth')


    return app
