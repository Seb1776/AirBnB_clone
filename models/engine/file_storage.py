#!/usr/bin/python3
""" Class FileStorage """

import json
import models
from models.base_model import BaseModel
from datetime import datetime
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    FileStorage that serializes instances to a JSON
    file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return the dictionary """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        new_dict = {}
        for key in self.__objects.keys():
            new_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        to_deserialize = {"BaseModel": BaseModel, "User": User,
                          "Place": Place, "State": State, "City": City,
                          "Amenity": Amenity, "Review": Review}

        try:
            tmp = {}

            with open(FileStorage.__file_path, 'r') as file:
                tmp = json.load(file)

                for key, val in tmp.items():
                    self.all()[key] = to_deserialize[val['__class__']](**val)
        except FileNotFoundError:
            pass
