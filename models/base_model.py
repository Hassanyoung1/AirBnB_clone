#!/usr/bin/env python3
"""
base_model module: contains a class `BaseModel` that defines common
attributes/methods for other classes in the AirBnB project.

You can test this module using the following command:
python3 -m unittest tests/test_models/test_base_model.py
"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """
    BaseModel class: defines all common attributes/methods for other classes

    Attributes:
        id (str): Unique identifier for each instance.

        created_at (datetime): The date and time
        when the instance was created.

        updated_at (datetime): The date and time when the
        instance was last updated.

    Methods:
        __init__: initializes a new instance of BaseModel

        __str__: returns an informal string representation of an instance

        save: updates the public instance attribute `updated_at` with
        the current datetime

        to_dict: returns a dictionary containing all keys/values of
        __dict__ of the instance
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a BaseModel instance

        Args:
            id (str): Assigned with a unique identifier when an
            instance is created.

            created_at (datetime): Assigned with the current
            datetime when an instance is created.


            updated_at (datetime): Assigned with the current
            datetime when an instance is created
            and updated every time you change your object.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns an informal string representation of an instance

        Returns:
            str: String representation of BaseModel attributes
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute `updated_at` with
        the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        __dict__ of the instance

        Returns:
            dict: Dictionary containing the attributes of BaseModel
        """
        dicts = self.__dict__.copy()
        dicts["__class__"] = self.__class__.__name__
        dicts["created_at"] = self.created_at.isoformat()
        dicts["updated_at"] = self.updated_at.isoformat()
        return dicts
