#!/usr/bin/python3
''' Defines a user '''

from models.base_model import BaseModel

class User(BaseModel):
    '''Represents a user class
    Attributes:
             email(str): user's email
             passwd(sttr): user's password
             first_name(str): user's first name
             last_name(str): user's last name
    '''
    email = ''
    passwd = ''
    first_name = ''
    last_name = ''
