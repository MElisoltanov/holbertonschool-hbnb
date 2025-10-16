<<<<<<< HEAD
from .BaseModel import BaseModel


class Amenity(BaseModel):
    def __init__(self, name):
=======
from app.models.BaseModel import BaseModel


class Amenity(BaseModel):

    def __init__(self, name):

>>>>>>> 9c096d260c12950a83daef36b736d51f6ec690fc
        super().__init__()
        self.set_name(name)

    def set_name(self, name):
<<<<<<< HEAD
=======

>>>>>>> 9c096d260c12950a83daef36b736d51f6ec690fc
        if not name:
            raise ValueError("Amenity name is required.")
        if len(name) > 50:
            raise ValueError("Amenity name must be 50 characters or fewer.")
        self.name = name
        self.save()  # Update updated_at timestamp from BaseModel

<<<<<<< HEAD
    def __str__(self):
=======
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def __str__(self):

>>>>>>> 9c096d260c12950a83daef36b736d51f6ec690fc
        return "Amenity(id={}, name={})".format(self.id, self.name)
