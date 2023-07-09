#!/usr/bin/python3
"""comments"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """comments"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """comments"""

        return self.__objects

    def new(self, obj):
        """comments"""

        if obj is not None:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """comments"""

        with open(self.__file_path, 'w') as f:
            objects_json = {}
            for key, value in self.__objects.items():
                objects_json[key] = value.to_dict()
            json.dump(objects_json, f)

    def path(self):
        """Devuelve la ruta del archivo JSON."""
        return self.__file_path

    def reload(self):
        """comments"""

        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                objects_json = json.load(f)
                for key, value in objects_json.items():
                    obj_class = value['__class__']
                    obj = eval(obj_class + "(**value)")
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
