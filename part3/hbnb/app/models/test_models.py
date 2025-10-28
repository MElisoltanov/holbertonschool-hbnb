from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity


def test_all_models():
    # 1️⃣ Create a User
    user = User(first_name="Alice", last_name="Smith", email="alice@example.com")
    assert user.first_name == "Alice"
    assert user.email == "alice@example.com"

    # 2️⃣ Create a Place owned by the user
    place = Place(
        title="Cozy Apartment",
        description="A nice place to stay",
        price=120,
        latitude=37.7749,
        longitude=-122.4194,
        owner=user
    )
    assert place.owner == user
    assert place.title == "Cozy Apartment"

    # 3️⃣ Create some Amenities and add them to the place
    wifi = Amenity(name="Wi-Fi")
    parking = Amenity(name="Parking")
    place.add_amenity(wifi)
    place.add_amenity(parking)

    assert len(place.amenities) == 2
    assert place.amenities[0].name == "Wi-Fi"
    assert place.amenities[1].name == "Parking"

    # 4️⃣ Create a Review and link it to the Place and User
    review = Review(user_id=user.id, place_id=place.id, text="Fantastic stay!", rating=5)
    place.add_review(review)

    assert len(place.reviews) == 1
    assert place.reviews[0].text == "Fantastic stay!"
    assert place.reviews[0].rating == 5
    assert place.reviews[0].place_id == place.id
    assert place.reviews[0].user_id == user.id

    print("✅ All model creation and relationships test passed!")


# Run directly
if __name__ == "__main__":
    test_all_models()

