#!/usr/bin/python3
"""Define File Storage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represents storage engine

    Attributes:
        __file_path (str): Name of file to save object
        __objects(dict): A dictionary
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets objects with key"""
        objectClass = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objectClass, obj.id)] = obj

    def save(self):
        """Serialize objects with JSON file"""
        o_dict = FileStorage.__objects
        o_dict_bef_serl = {obj: o_dict[obj].to_dict() for obj in o_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(o_dict_bef_serl, f)

    def reload(self):
        """Deserialization of the JSON file"""
        try:
            with open(FileStorage.__file_path) as f:
                o_dict_bef_serl = json.load(f)
                for o in o_dict_bef_serl.values():
                    className = o.get["__class__"]
                    if className:
                        del o["__class__"]
                        class_obj = globals().get(className)
                        if class_obj:
                            self.new(class_obj(**o))
                        else:
                            print("Class {} not found.".format(className))
                    else:
                        print("__class__ key not found in the object.")
        except Exception as e:
            print("An error occurred: {}".format(e))
