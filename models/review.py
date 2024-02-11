review.py
#!/usr/bin/python3
"""Definition of child class Review"""
from models.base_model import BaseModel


class Review(BaseModel):

    place_id = ""
    user_id = ""
    text = ""
