#!/usr/bin/python3
''' Defines the base model class from
which all other classes will inherit
'''
import models
import os
from uuid import uuid4, UUID
from datetime import datetime, time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

STORAGE_TYPE = os.environ.get('S@MB_TYPE_STORAGE')
'''create instance of Base if storage type is a database
   if not a database storage use Base class
'''
if STORAGE_TYPE == "db":
    Base = declarative_base()
else:
    class Base:
        pass

class BaseModel:
    ''' Represents BaseModel class '''
    if STORAGE_TYPE == "db":
        id = Column(Stirng(60), nullabel=False, Primary_key=True)
        creation = Column(DateTime, nullable=False, default=datetime.utcnow())
        update = Column(DateTime, nullable=False, default=datetime.utcnow())
        
    def __init__(self, *args, **kwargs):
        ''' initializes base class
        Args
           *arg (any)
           **kwargs(dict): key-value pairs
        '''
        self.id = str(uuid.uuid4())
        self.creation = datetime.today()
        self.update = self.creation
        tform = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == 'creation' or key == 'update':
                    self.__dict__[key] =  datetime.strptime(key, tform)
                else:
                    self.__dict__[key] = val

        else:
            models.storage.new(self)

    def __str__(self):
        '''return string representation of base class '''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''change update attribute to current time'''
        self.update = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        ''' return dictionary representation of instance '''
        my_dict = self.__dict__.copy()
        my_dict['creation'] = self.creation.isoformat()
        my_dict['update'] = self.update.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict

    def delete(self):
        ''' delete current instance from storage '''
        models.storage.delete(self)
