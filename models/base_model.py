#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """
    The BaseModel class defines a basic model with common
    attributes and methods for other classes.

    Attributes:
        id (str): A unique identifier generated using uuid4().
        created_at (datetime): The timestamp indicating
        the object's creation time.
        updated_at (datetime): The timestamp indicating the
        object's last modification time.

    Methods:
        __init__(): Initializes a new BaseModel instance with a unique ID,
        creation, and update timestamps.
        __str__(): Returns a string representation of the BaseModel object.
        save(): Updates the `updated_at` attribute to the current timestamp.
        to_dict(): Converts the BaseModel object to a dictionary representation
    """

    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs != {}:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.created_at = datetime.now()
            self.id = str(uuid4())
            """
            Initializes a new BaseModel instance.
            """
    def __str__(self):
        """
        Returns a string representation of the BaseModel object.

        Returns:
            str: A formatted string containing the class name, ID,
            and dictionary representation.
        """
        return "[{}] ({}) {}".format(__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates the `updated_at` attribute to the current timestamp.
        """
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        self.__dict__["__class__"] = __class__.__name__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__
