from app.persistence.user_repository import UserRepository
from app.persistence.repository import SQLAlchemyRepository
from app.models.user import User
from app.models.place import Place
from app.models.amenity import Amenity
from app.models.review import Review
from app.Extensions import db

class HBnBFacade:
    def __init__(self):

        self.user_repo = UserRepository()
        self.place_repo = SQLAlchemyRepository(Place)
        self.review_repo = SQLAlchemyRepository(Review)
        self.amenity_repo = SQLAlchemyRepository(Amenity)

    # =====================
    # User facade
    # =====================
    def create_user(self, user_data):
        user = User(**user_data)
        user.hash_password(user_data['password'])
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_user_by_email(email)

    def get_all_users(self):
        return self.user_repo.get_all()
    
    def update_user(self, user_id, data):
        user = self.get_user(user_id)
        if not user:
            return None

        # Update allowed fields
        if "email" in data and data["email"] is not None:
            user.email = data["email"]

        if "password" in data and data["password"] is not None:
            user.hash_password(data["password"])

        if "name" in data and data["name"] is not None:
            user.name = data["name"]

        if "is_admin" in data:
            user.is_admin = data["is_admin"]

        db.session.commit()
        return user

    # =====================
    # Place facade
    # =====================
    def create_place(self, place_data):
        owner_id = place_data.get("owner_id")
        if not owner_id:
            raise ValueError("owner_id is required")
        owner = self.user_repo.get(owner_id)
        if not owner:
            raise ValueError("Owner not found")

    # Create the place first (without amenities)
        new_place = Place(
            title=place_data.get("title"),
            description=place_data.get("description"),
            price=place_data.get("price"),
            latitude=place_data.get("latitude"),
            longitude=place_data.get("longitude"),
            owner_id=owner_id
        )
        self.place_repo.add(new_place)

        # Safely attach amenities (handles both IDs and objects)
        amenity_ids = place_data.get("amenities") or []
        amenity_objs = []
        for a in amenity_ids:
            if isinstance(a, Amenity):
                amenity_objs.append(a)
            else:
                amenity = self.amenity_repo.get(a)
                if amenity:
                    amenity_objs.append(amenity)

        if amenity_objs:
            new_place.amenities = amenity_objs
            db.session.commit()

        return new_place
        '''# transformed ID into objects Amenity
        amenities = place_data.get("amenities") or []
        amenities_objs = [self.amenity_repo.get(a_id) for a_id in amenities]


        new_place = Place(
            place_data.get("title"),
            place_data.get("description"),
            place_data.get("price"),
            place_data.get("latitude"),
            place_data.get("longitude"),
            owner_id,
            amenities_objs
        )
        self.place_repo.add(new_place)
        return new_place'''

    def get_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError("Place not found")
        return place

    def get_all_places(self):
        return self.place_repo.get_all()
    #new update place
    def update_place(self, place_id, update_data):
        """Update an existing place with new data."""
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError("Place not found")

        # Handle amenities separately if passed
        if "amenities" in update_data:
            amenity_ids = update_data["amenities"] or []
            amenity_objs = []
            for a in amenity_ids:
                if isinstance(a, Amenity):
                    amenity_objs.append(a)
                else:
                    amenity = self.amenity_repo.get(a)
                    if amenity:
                        amenity_objs.append(amenity)
            place.amenities = amenity_objs

        # Update fields safely
        for key, value in update_data.items():
            if hasattr(place, key):
                setattr(place, key, value)

        

        db.session.commit()
        return place
    
    def delete_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            return None

        db.session.delete(place)
        db.session.commit()
        return place

    # =====================
    # Review facade
    # =====================
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
        return [review for review in self.review_repo.get_all() if review.place_id == place_id]
    
    def update_review(self, review_id, data):
        review = self.review_repo.get(review_id)
        if not review:
            return None

        # Update allowed fields only
        if "text" in data and data["text"] is not None:
            review.text = data["text"]

        if "rating" in data and data["rating"] is not None:
            rating = data["rating"]
            if not (1 <= rating <= 5):
                raise ValueError("Rating must be between 1 and 5")
            review.rating = rating

            db.session.commit()
            return review

    ##new

    # =====================
    # Amenity facade
    # =====================
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity
    #new one gey amme
    def get_amenity(self, amenity_id):
        if isinstance(amenity_id, Amenity):
            amenity_id = amenity_id.id
        return self.amenity_repo.get(amenity_id)
    #old get amme
    """def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)"""

    def get_all_amenities(self):
        return self.amenity_repo.get_all()
    
    def get_user_review_for_place(self, user_id, place_id):
        return Review.query.filter_by(user_id=user_id, place_id=place_id).first()
    
    def update_amenity(self, amenity_id, data):
        amenity = self.get_amenity(amenity_id)
        if not amenity:
            return None

        # Update only allowed fields
        if "name" in data and data["name"] is not None:
            amenity.name = data["name"]

        db.session.commit()
        return amenity
