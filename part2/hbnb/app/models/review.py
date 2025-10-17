from app.models.BaseModel import BaseModel


class Review(BaseModel):

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
        return "Review(id={}, rating={}, place_id={}, user_id={})".format(
            self.id, self.rating, self.place_id, self.user_id)
