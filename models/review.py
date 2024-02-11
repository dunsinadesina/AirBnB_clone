review.py
#!/usr/bin/python3
"""Definition of child class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class.

    Attributes:
        place_id (str): id of place.
        user_id (str): id of user.
        text (str): review by user.
    """

    place_id = ""
    user_id = ""
    text = ""
