#!/usr/bin/env python3

from .base_model import BaseModel


class Review(BaseModel):
    """
    Review class: represents user reviews for places in the AirBnB project.

    Attributes:
        place_id (str): The ID of the place associated with the review.
        user_id (str): The ID of the user who created the review.
        text (str): The content of the review.

    Methods:
        __init__: initializes a new instance of Review,
          inherits attributes from BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a Review instance

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
