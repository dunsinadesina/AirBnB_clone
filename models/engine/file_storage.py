#!/usr/bin/python3
"""Parent class for data management"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:

    __file_path = "file.json"
    __objs = {}

    def all(self):
        """Return the dictionary objects."""
        return FileStorage.__objs

    def new(self, obj):
        """Sets key pair value of object obj"""
        ocname = obj.__class__.__name__
        FileStorage.__objs["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Function serializes data and returns in the created dict"""
        odict = FileStorage.__objs
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """This function desserializes json file and returns if exception occcurs"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except:
            return
