#!/usr/bin/python3
"""document AirBnb"""


import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        
    def update(self):
        self.updated_at = datetime.now()
    
    def save(self):
        self.update()
        
    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
    
    def __str__(self):
        class_name = self.__class__.__name__
        obj_id = self.id
        obj_dict = self.__dict__
        return "[{}] ({}) {}".format(class_name, obj_id, obj_dict)
    
