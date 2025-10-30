from app.models.BaseModel import BaseModel
from app.Extensions import db


class Amenity(BaseModel):
    __tablename__ = 'amenities'

    name = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, name):
        super().__init__()
        self.set_name(name)

    def set_name(self, name):
        if not name:
            raise ValueError("Amenity name is required.")
        if len(name) > 50:
            raise ValueError("Amenity name must be 50 characters or fewer.")
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def __str__(self):
        return f"Amenity(id={self.id}, name={self.name})"