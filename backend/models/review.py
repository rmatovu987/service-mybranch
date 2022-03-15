#!/usr/bin/env python3
"""Defines the Review class """

import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import *
from sqlalchemy.orm import relationship

STORAGE_TYPE = os.environ.get('SAMB_TYPE_STORAGE')

class Review(BaseModel):
    """Represents a review
    Attributes:
           branch_id(str): the branch id
           user_id(str): the user id
           text(str): the review
    """
    if STORAGE_TYPE == 'db':
        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        brank_id = Column(String(60), ForeignKey('brank.id'), nullable=False)
        branch_id = Column(String(60), ForeignKey('branch.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        bank_id = ""
        branch_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        '''initialize reviews object'''
        super().__init__(*args, **kwargs)
