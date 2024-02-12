#!/usr/bin/python3
"""Definition child class place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class.

    Attributes:
        city_id (str): id of city.
        user_id (str): identification of user.
        name (str): place name.
        description (str): place description.
        number_rooms (int): amount of rooms in the place.
        number_bathrooms (int): amount of bathrooms in the place.
        max_guest (int): max number of quests.
        price_by_night (int): price for booking per night.
        latitude (float): place lattitude.
        longitude (float): place longitude.
        amenity_ids (list): amenity ids.
     """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
