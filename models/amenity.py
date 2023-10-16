#!/usr/bin/env python3

"""
amenity module: contains the Amenity class
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class: represents amenities available
    in accommodations in the AirBnB project.

    Attributes:
        name (str): The name of the amenity.

    Methods:
        __init__: initializes a new instance of Amenity,
                  inherits attributes from BaseModel
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize an Amenity instance

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
