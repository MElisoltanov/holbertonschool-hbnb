from app.models.BaseModel import BaseModel
from app.Extensions import db
from app.models.place_amenity import place_amenity


class Place(BaseModel):
    __tablename__ = 'places'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    # Foreign key
    owner_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)

    # Relationships
    amenities = db.relationship(
        'Amenity',
        secondary=place_amenity,
        backref=db.backref('places', lazy=True),
        lazy='subquery'
    )
    reviews = db.relationship('Review', backref='place', lazy=True)

    def __init__(self, title, description, price, latitude, longitude, owner_id, amenities=None):
        super().__init__()

        if not title or len(title) > 100:
            raise ValueError("Title is required and must be 100 characters max.")
        if price <= 0:
            raise ValueError("Price must be positive.")
        if not (-90 <= latitude <= 90):
            raise ValueError("Latitude must be between -90 and 90.")
        if not (-180 <= longitude <= 180):
            raise ValueError("Longitude must be between -180 and 180.")
        if not owner_id:
            raise ValueError("Place must have an owner (User).")

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.amenities = amenities or []

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def __repr__(self):
        return f"<Place {self.title}>"
