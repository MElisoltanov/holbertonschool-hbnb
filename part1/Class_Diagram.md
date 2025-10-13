## Class Diagram

```mermaid
---
config:
  look: neo
  layout: elk
  theme: neo
---
classDiagram
direction BT

class BaseModel {
    +UUID id
    +datetime created_at
    +datetime updated_at
    +create()
    +read()
    +update()
    +save()
    +delete()
}

class User {
    +string first_name
    +string last_name
    +string email
    +string password
    +bool is_admin
    +string payment_method
}

class Place {
    +UUID user_id
    +string title
    +string description
    +float price
    +float latitude
    +float longitude
    +int rooms
    +int capacity
    +float area
}

class Review {
    +UUID user_id
    +UUID place_id
    +string title
    +string text
    +int rating
}

class Amenity {
    +string name
}

User --|> BaseModel
Place --|> BaseModel
Review --|> BaseModel
Amenity --|> BaseModel

User "1" --> "0..*" Place : creates
Place "1" --> "0..*" Review : receives
Place "1..*" o-- "1..*" Amenity : has
