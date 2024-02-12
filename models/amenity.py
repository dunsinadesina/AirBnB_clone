#!/usr/bin/python3
"""Definitin of class Amnesty that inherits from basemodel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity cls.

    Attributes:
        name (str): amenity name.
    """

    name = ""
