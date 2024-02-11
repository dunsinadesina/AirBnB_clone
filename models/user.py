#!/usr/bin/python3
"""This program contains definatipon of user class and inherits from basemodel"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class.

    Attributes:
        email (str): User email address
        password (str): user access str
        first_name (str): user birth name
        last_name (str): user surname
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
