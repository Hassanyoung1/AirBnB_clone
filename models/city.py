#!/usr/bin/env python3

"""
City Module
===========

This module contains the City class, which
represents cities in the AirBnB project.

Classes:
    City: Represents a city with attributes like state_id and name.

Usage:
    To create a new city instance:
    >>> city = City()

    You can also specify attributes during initialization:
    >>> city = City(state_id='123', name='Example City')
"""

from .base_model import BaseModel


class City(BaseModel):
    """
    City class: represents cities in the AirBnB project.

    Attributes:
        state_id (str): The ID of the state to which the city belongs.
        name (str): The name of the city.

    Methods:
        __init__: initializes a new instance of City,
        inherits attributes from BaseModel
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a City instance

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
