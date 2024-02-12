#!/usr/bin/python3
"""Definition of class city that inherits from basmodel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class that represnts the Cityclass.

    Atrributes:
        state_id: state_id: string - empty string: it will be the State.id
        name:  string - empty string
    """

    state_id = ""
    name = ""
