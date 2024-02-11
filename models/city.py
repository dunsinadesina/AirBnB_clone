city.py
#!/usr/bin/python3
"""Definition of class city that inherits from basmodel"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class.
    
    Atrributes:
        state_id (str) : id state.
        name (str): city name.
    """

    state_id = ""
    name = ""
