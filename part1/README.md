# Class Diagram update

Here’s how your final diagram entities connect to your Python implementation:


| **UML Class**            | **Python File**                                   | **Key Relationships**                                   |
| :-----------------: | ------------------------------------------------- |------------------------------------------------- |
| `BaseModel`       | models/BaseModel.py	.                          |Inherited by all|
| `User`     | models/user.py.                        |user.places[], user.reviews[]|
| `Place`      | models/place.py. |place.user_id, place.reviews[], place.amenities[]|
| `Review`       | models/review.py     |review.place_id, review.user_id|
| `Amenity `       | models/amenity.py    | Many-to-many with Place|



Good                                Improve
Inheritance structure	            Remove redundant Id* attributes
Relationships defined	            Adjust Amenity to many-to-many
Attributes typed	                Replace Owner object with user_id

## 📄 <span id="Multiplicity">Multiplicity</span>
How many objects of each class take part in the relationships and multiplicity can be expressed as:

Exactly one - 1

Zero or one - 0..1

Many - 0..* or *

One or more - 1..*

Exact Number - e.g. 3..4 or 6

Or a complex relationship - e.g. 0..1, 3..4, 6.* would mean any number of objects other than 2 or 5