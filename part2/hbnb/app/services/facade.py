from app.persistence.repository import InMemoryRepository
from app.models.place import Place
from app.models.user import User
from app.models.amenity import Amenity
from app.models.review import Review


class HBnBFacade:
    user_repo = InMemoryRepository()
    place_repo = InMemoryRepository()
    review_repo = InMemoryRepository()
    amenity_repo = InMemoryRepository()

    def __init__(self):
        pass

    def create_place(self, place_data):
        # Validate owner exists instead of creating a temporary user
        owner_id = place_data.get("owner_id")
        if not owner_id:
            raise ValueError("owner_id is required")
        owner = self.user_repo.get(owner_id)
        if not owner:
            raise ValueError("Owner not found")

        amenities = place_data.get("amenities") or []

        new_place = Place(
            place_data.get("title"),
            place_data.get("description"),
            place_data.get("price"),
            place_data.get("latitude"),
            place_data.get("longitude"),
            owner_id,
            amenities
        )

        self.place_repo.add(new_place)
        return new_place

    def get_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError("Place not found")
        return place

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError("Place not found")

        for key, value in place_data.items():
            if hasattr(place, key):
                setattr(place, key, value)
        return place

    """user facade"""

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        return self.user_repo.get_all()

    """Amenity facade """

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return None
        for key, value in amenity_data.items():
            setattr(amenity, key, value)
        # pass a dict to repository.update for consistency
        self.amenity_repo.update(amenity.id, {'name': amenity.name})
        return amenity

    """Review facade"""

    def create_review(self, review_data):
        user_id = review_data.get('user_id')
        place_id = review_data.get('place_id')
        rating = review_data.get('rating')
        text = review_data.get('text')

        if not user_id or not place_id or rating is None:
            raise ValueError("user_id, place_id, and rating are required")

        if not self.user_repo.get(user_id):
            raise ValueError("User not found.")
        if not self.place_repo.get(place_id):
            raise ValueError("Place not found.")

        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")

        review = Review(text=text, rating=rating, user_id=user_id, place_id=place_id)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        all_reviews = self.review_repo.get_all()
        return [r for r in all_reviews if r.place_id == place_id]

    def update_review(self, review_id, review_data):
        review = self.review_repo.get(review_id)
        if not review:
            return None

        if 'text' in review_data:
            review.text = review_data['text']
        if 'rating' in review_data:
            rating = review_data['rating']
            if not (1 <= rating <= 5):
                raise ValueError("Rating must be between 1 and 5.")
            review.rating = rating

        # pass a dict (not the object) to repository.update to match its contract
        self.review_repo.update(review_id, {'text': review.text, 'rating': review.rating})
        return review

    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            return False
        self.review_repo.delete(review_id)
        return True
