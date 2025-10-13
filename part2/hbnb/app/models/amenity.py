from app.models.BaseModel import BaseModel

class amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name
