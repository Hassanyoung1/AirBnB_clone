#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

"""Serializes instances to a JSON file
and derializes an instances from a JSON file"""


class FileStorage:
    """Class declaration for FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self, class_name=None):
        """Returns the dictionary __objects"""
        if class_name is not None:
            if isinstance(class_name, str):
                try:
                    cls = eval(class_name)
                except NameError:
                    raise ValueError("Invalid class name")

            filtered_objs = {k: v for k, v in FileStorage.__objects.items()
                             if isinstance(v, cls)}
            return filtered_objs

        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj
        with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        dict = FileStorage.__objects
        objdict = {obj: dict[obj].to_dict() for obj in dict.keys()}
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(objdict, file)

    def reload(self):
        """Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                desirlized = json.load(file)
                for x in desirlized.values():
                    cls_name = x["__class__"]
                    del x["__class__"]
                    self.new(eval(cls_name)(**x))
        except FileNotFoundError:
            return
