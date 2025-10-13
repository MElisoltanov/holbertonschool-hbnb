from app.models.BaseModel import BaseModel

class review(BaseModel):
    def __init__(self, title, text, rating):
        super().__init__()
        self.title = title
        self.text = text
        self.rating = rating
        self.place = []  # List to store related reviews
