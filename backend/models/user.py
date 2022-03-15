#!/usr/bin/python3
''' Defines a user '''
import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import *
from sqlalchemy.orm import relationship
import hashlib

STORAGE_TYPE = os.environ.get('SAMB_TYPE_STORAGE')

class User(BaseModel, Base):
    '''Represents a user class
    Attributes:
             email(str): user's email
             passwd(sttr): user's password
             first_name(str): user's first name
             last_name(str): user's last name
    '''
    if STORAGE_TYPE == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        branch = relationship('Branch', backref='user', cascade='delete')
        review = relationship('Review', backref='user', cascade='delete')
    else:
        email = ''
        passwd = ''
        first_name = ''
        last_name = ''

    def __init__(self, *args,**kwargs):
        """initialize user object"""
        super().__init__(*args, **kwargs)

    def __set_password(self, pwd):
        '''custom password setter that encrypts with MD5'''
        secure - hashlib.md5()
        secure.update(pwd.encode('utf-8'))
        secure_password = secure.hexidigest()
        setattr(self, "password", secure_password)
