#!/usr/bin/python3
import json
from os.path import exists
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        class_name = __class__.__name__
        key = class_name + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        serilized_obj = {}
        for key, obj in FileStorage.__objects.items():
            serilized_obj[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serilized_obj, file)

    def reload(self):
        if exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path,
                          "r", encoding='utf-8') as file:
                    lds = json.load(file)
                    for key, value in lds.items():
                        FileStorage.__objects[key] = BaseModel(**value)
            except FileNotFoundError:
                pass
