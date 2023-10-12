#!/usr/bin/python3

class FileStorage:


    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name,obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serilized_obj = {}
        for key, obj in FileStorage.__objects.items():
            serilized_obj[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding=utf-'8') as file:
            json.dump(serilized_obj, file)
    def reload(self):
        try:
            with open(__file_path, 'r', encoding=utf-'8') as file:
                data = json.load(file)
                for key, value in data.items():
                    obj_id = key.split('')
        except FileNotFoundError:
            pass
