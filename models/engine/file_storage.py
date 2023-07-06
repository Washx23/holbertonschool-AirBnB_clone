#!/usr/bin/python3
"""document File storage"""

import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)
            
    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                serialized_objects = json.load(file)
                for key, obj_dict in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    obj = BaseModel(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

        

