#!/usr/bin/python3
"""document AirBnb"""


import uuid
from datetime import datetime
import models


class BaseModel:

    def __init__(self, *args, **kwargs):
        """ Construct """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if 'id' not in kwargs.keys():
                    self.id = str(uuid.uuid4())
                if 'created_at' not in kwargs.keys():
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs.keys():
                    self.updated_at = datetime.now()
                setattr(self, key, value)
        models.storage.new(self)

    def update(self):
        "document"
        self.updated_at = datetime.now()

    def __str__(self):
        "document"
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        "document"
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Return a dictionary representation of the object """
        if isinstance(self, BaseModel):
            obj_dict = self.__dict__.copy()
            obj_dict['__class__'] = self.__class__.__name__
            obj_dict['created_at'] = self.created_at.isoformat()
            obj_dict['updated_at'] = self.updated_at.isoformat()
            return obj_dict
        else:
            return self.copy()
