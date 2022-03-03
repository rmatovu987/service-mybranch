#!/usr/bin/env python3
"""Defines the Review class """

from models.base_model import BaseModel

class Review(BaseModel):
    """Represents a review
    Attributes:
           branch_id(str): the branch id
           user_id(str): the user id
           text(str): the review
    """
    branch_id = ""
    user_id = ""
    text = ""
