#!/usr/bin/python3
"""This module defines a class to manage file storage"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """
    FileStorage class
    """

    __file_path = "file.json"
    __objects = {}


    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file exists;
        otherwise, do nothing). If the JSON file doesn't exist, it's not an error.
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                objects = json.load(file)
                for key, value in objects.items():
                    cls_name = value['__class__']
                    obj = eval(cls_name + '(**value)')
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def close(self):
        """
        Deserializes the JSON file to objects and calls reload() method.
        """
        self.reload()
