#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """
    This User class is a subclass of BaseModel.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
