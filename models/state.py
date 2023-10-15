#!/usr/bin/env python3

from .base_model import BaseModel

""" Declare the class """


class State(BaseModel):
    """
    State class: represents states in the AirBnB project.

    Attributes:
        name (str): The name of the state.

    Methods:
        __init__: initializes a new instance of State,
        inherits attributes from BaseModel
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a State instance

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
