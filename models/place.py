#!/usr/bin/env python3

from .base_model import BaseModel


class Place(BaseModel):
    """
    Place class: represents information about accommodations in
      the AirBnB project.

    Attributes:
        city_id (str): The ID of the city where the place is located.

        user_id (str): The ID of the user who owns the place.

        name (str): The name of the place.

        description (str): A description of the place.

        number_rooms (int): The number of rooms in the place.

        number_bathrooms (int): The number of bathrooms in the place.

        max_guest (int): The maximum number of guests
        the place can accommodate.

        price_by_night (int): The price per night to stay at the place.

        latitude (float): The latitude coordinate of the place.

        longitude (float): The longitude coordinate of the place.

        amenity_ids (str): A string representing Amenity IDs associated
        with the place.

    Methods:
        __init__: initializes a new instance of Place,
        inherits attributes from BaseModel
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a Place instance

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
