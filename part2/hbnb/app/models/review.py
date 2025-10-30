from app.models.BaseModel import BaseModel
from app.Extensions import db


class Review(BaseModel):
    __tablename__ = "reviews"
    
    text = db.Column(db.String(1024), nullable=False)
    rating = db.Column(db.Integer, nullable=False, default=5)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    place_id = db.Column(db.String(36), db.ForeignKey('places.id'), nullable=False)

    __table_args__ = (
        db.UniqueConstraint('user_id', 'place_id', name='unique_user_place_review'),
    )

    def __init__(self, user_id, place_id, text, rating=5, **kwargs):
        super().__init__(**kwargs)

        if not text or not isinstance(text, str):
            raise ValueError("Text cannot be empty and must be a string.")
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise ValueError("Rating must be an integer between 1 and 5.")

        self.user_id = user_id
        self.place_id = place_id
        self.text = text
        self.rating = rating

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "place_id": self.place_id,
            "text": self.text,
            "rating": self.rating,
        }

    def __str__(self):
        return f"Review(id={self.id}, rating={self.rating}, place_id={self.place_id}, user_id={self.user_id})"