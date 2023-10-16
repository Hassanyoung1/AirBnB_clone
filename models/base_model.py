#!/usr/bin/python3
import uuid
from datetime import datetime
format_datetime = "%Y-%m-%dT%H:%M:%S.%f"

"""Define BaseModel class"""


class BaseModel:
    """Class declaration for baseModel of the clone"""
    def __init__(self, *args, **kwargs):
        """Initializes a new instant.

        Args:
        args: unused
        kwargs: key/value pair of arguments
        """
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__['created_at'] = datetime.strptime(
                     kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__['updated_at'] = datetime.strptime(
                     kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def to_dict(self):
        """Dictionary containing all keys/values
        of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

    def save(self):
        """Updates the public instance attribute
        updated_at with the current datetime"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """String representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
    