#!/usr/bin/python3
''' Defines a Bank Branch model '''

from models.base_model import BaseModel

class Branch(BaseModel):
    ''' Represents a bank branch class
    Attributes:
            bank_id(str): the bank id
            branch_name(str): The branch name
    '''
    bank_id = ''
    branch_name = ''
    
