#!/usr/bin/python3
''' Defines Bank Model '''

import models
from models.base_model import BaseModel, Base
import os
from sqlalchemy import *
from sqlalchemy.orm import relationship

STORAGE_TYPE = os.environ.get("SAMB_TYPE_STORAGE")

class Bank(BaseModel, Base):
    '''Represents a bank class
    Attributes:
            bank_name(str): the name of the bank
    '''
    if STORAGE_TYPE == 'db':
        __tablename__ = 'banks'
        bank_name = Column(String(128), nullable=False)
        branches = relationship('Branch', backref='bank', cascade='delete')
    else:
        bank_name = ''

    def __init__(self, *args, **kwargs):
        ''' initialize bank '''
        super().__init__(*args, **kwargs)

    @property
    def branches(self):
        ''' method to return branch objects related to the bank '''
        branch_list = []
        for branch in models.storage.all("Branch").values():
            if branch.bank_id == self.id:
                branch_list.append(branch)
        return branch_list
