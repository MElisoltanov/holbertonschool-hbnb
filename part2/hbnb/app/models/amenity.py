from .BaseModel import BaseModel


class Amenity(BaseModel):
    """
    Represents an Amenity with a unique ID and a validated name.

    Attributes:
        id (str): Unique identifier inherited from BaseModel.
        name (str): Name of the amenity. Required, max 50 characters.
    """

    def __init__(self, name):
        """
        Initialize a new Amenity instance.

        Args:
            name (str): The name of the amenity.

        Raises:
            ValueError: If name is empty or longer than 50 characters.
        """
        super().__init__()
        self.set_name(name)

    def set_name(self, name):
        """
        Validate and set the amenity name.

        Args:
            name (str): The new name to set.

        Raises:
            ValueError: If name is empty or exceeds 50 characters.
        """
        if not name:
            raise ValueError("Amenity name is required.")
        if len(name) > 50:
            raise ValueError("Amenity name must be 50 characters or fewer.")
        self.name = name
        self.save()  # Update updated_at timestamp from BaseModel

    def __str__(self):
        """
        Return a string representation of the Amenity.

        Returns:
            str: String showing id and name.
        """
        return "Amenity(id={}, name={})".format(self.id, self.name)
