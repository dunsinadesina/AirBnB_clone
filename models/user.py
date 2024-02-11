#!/usr/bin/python3
"""This program contains definatipon of user class and inherits from basemodel"""
from models.base_model import BaseModel


class User(BaseModel):
    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""
