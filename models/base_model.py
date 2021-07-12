#!/usr/bin/python3
""" Base Model Object """

import uuid
from datetime import datetime
import models


class BaseModel:
    """ BaseModel Class """

    def __init__(self, *args, **kwargs):
        """
        Initializer
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if len(kwargs) is not 0:
            kwargs["created_at"] = datetime.strptime(kwargs.get("created_at"),
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs.get("updated_at"),
                                                     "%Y-%m-%dT%H:%M:%S.%f")
        for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)
        else:
            models.storage.new(self)

    def __str__(self):
        """
        String representation of BaseModel
        Return: String representation of BaseModel Object
        """
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__))

    def save(self):
        """
        Update the public instance attribute
        updated_at with the current datatime
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of __dict__ of instance.
        """
        my_dict = dict(self.__dict__)
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
