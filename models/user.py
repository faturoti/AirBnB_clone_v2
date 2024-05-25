#!/usr/bin/python3

"""User class for initiating Users"""

from models.base_model import BaseModel

class User(BaseModel):
    """For User rep

    Attributes:
        email (str): user email
        password (str): user password
        first_name (str): first name
        last_name (str): last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
