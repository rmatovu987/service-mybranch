#!/usr/bin/python3
''' Defines a Bank Branch model '''
import models
import os
from models.base_model import BaseModel, Base
from sqlalchemy import *
from sqlalchemy.orm import *

STORAGE_TYPE = os.environ.get('SAMB_TYPE_STORAGE')
class Branch(BaseModel, Base):
    ''' Represents a bank branch class
    Attributes:
            bank_id(str): the bank id
            branch_name(str): The branch name
    '''
    if STORAGE_TYPE == "db":
        __tablename__ = 'branches'
        branch_name = Column(String(128), nullable=False)
        bank_id = Column(String(60), ForeignKey('bank.id'), nullable=False)
    else:
        bank_id = ''
        branch_name = ''
    
