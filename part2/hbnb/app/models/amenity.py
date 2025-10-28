from app.models.BaseModel import BaseModel


class Amenity(BaseModel):

    def __init__(self, name):

        super().__init__()
        self.set_name(name)

    def set_name(self, name):
<<<<<<< HEAD
=======

>>>>>>> 8f49bfc437256fd86f415bc5296caa75e64161e1
        if not name:
            raise ValueError("Amenity name is required.")
        if len(name) > 50:
            raise ValueError("Amenity name must be 50 characters or fewer.")
        self.name = name
        self.save()  # Update updated_at timestamp from BaseModel

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def __str__(self):

        return "Amenity(id={}, name={})".format(self.id, self.name)
