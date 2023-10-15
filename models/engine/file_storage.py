#!/usr/bin/python3
import json
from os.path import exists
from models.base_model import BaseModel


class FileStorage:
    """
    This class manages the serialization and deserialization of instances
    into JSON format and vice versa. It uses a dictionary (__objects) to store
    instances and their corresponding keys for easy access.

    Attributes:
        __file_path (str): The file path to the JSON file.
        __objects (dict): Dictionary to store instances in
        the format {"class_name.id": instance}.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects, which stores all instances.

        Returns:
            dict: A dictionary containing all instances.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the __objects dictionary.

        Args:
            obj (BaseModel): The object to be added.
        """
        class_name = obj.__class__.__name__
        key = class_name + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to JSON and saves it
          to the file specified by __file_path.

        """
        serialized_obj = {}
        for key, obj in FileStorage.__objects.items():
            serialized_obj[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_obj, file)

    def reload(self):
        """
        Deserializes the JSON file specified by __file_path
        and loads the instances into __objects.

        """
        if exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, "r",
                          encoding='utf-8') as file:
                    loaded_objs = json.load(file)
                    for key, value in loaded_objs.items():
                        FileStorage.__objects[key] = BaseModel(**value)
            except FileNotFoundError:
                pass
