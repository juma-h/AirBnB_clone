#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """
    This Review class is a subclass of BaseModel.
    """
    place_id = ""
    user_id = ""
    text = ""