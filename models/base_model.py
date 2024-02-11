#!/usr/bin/python3
"""The Base Model Class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """The class for the Base Model of the AirBnB Clone Project"""

    def __init__(self, *args, **kwargs):
        """Initialize a new Base Model

        Args:
            *args: unused argument
            **kwargs: value of pairs of argument dict
        """

        timeFormat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, timeFormat)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """updates the public instance
        attribute updated_at with the current datetime"""

        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing
        all keys/values of __dict__ of the instance"""

        resultDict = self.__dict__.copy()
        resultDict["created_at"] = self.created_at.isoformat()
        resultDict["updated_at"] = self.updated_at.isoformat()
        resultDict["__class__"] = self.__class__.__name__
        return resultDict

    def __str__(self):
        """Return the string representation of the Base Model"""
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)
