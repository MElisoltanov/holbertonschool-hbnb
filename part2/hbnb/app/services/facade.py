from app.persistence.repository import InMemoryRepository
from app.models.place import Place


class HBnBFacade:
        
    user_repo = InMemoryRepository()
    place_repo = InMemoryRepository()
    review_repo = InMemoryRepository()
    amenity_repo = InMemoryRepository()


    def __init__(self):
        pass

    def create_place(self, place_data):
        new_place = Place( 
        place_data.get("title"),
        place_data.get("description"),
        place_data.get("price"),
        place_data.get("latitude"),
        place_data.get("longitude")
        )

        self.place_repo.add(new_place)
        return (new_place)

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
