#!/usr/bin/python3
"""
Module containing the BaseModel class.
"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """
    BaseModel class: defines all common attributes
    /methods for other classes

    Attributes:
        id (str): unique identifier for each instance.

        created_at (datetime): datetime object representing
        the instance creation time.

        updated_at (datetime): datetime object representing the
        instance last update time.

    Methods:
        __init__(self, *args, **kwargs): initializes a new BaseModel instance.
        __str__(self): returns a string representation of
        the BaseModel instance.

        save(self): updates the public instance attribute
        `updated_at` with the current datetime.

        to_dict(self): returns a dictionary
        representation of the BaseModel instance.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: String representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute
        updated_at` with the current datetime.

        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Returns:
            dict: Dictionary containing the attributes of BaseModel.
        """
        dicts = self.__dict__.copy()
        dicts["__class__"] = self.__class__.__name__
        dicts["created_at"] = self.created_at.isoformat()
        dicts["updated_at"] = self.updated_at.isoformat()
        return dicts
