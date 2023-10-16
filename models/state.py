#!/usr/bin/env python3

"""
State Module: contains the State class that represents
states in the AirBnB project.
"""

from .base_model import BaseModel


class State(BaseModel):
    """
    State class: represents states in the AirBnB project.

    Attributes:
        name (str): The name of the state.

    Methods:
        __init__: initializes a new instance of State,
        inherits attributes from BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a State instance

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
