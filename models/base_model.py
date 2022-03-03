#!/usr/bin/python3
''' Defines the base model class from
which all other classes will inherit
'''
import models
from uuid import uuid4
from datetime import datetime, time

class BaseModel:
    ''' Represents base class '''
    def __init__(self, *args, **kwargs):
        ''' initializes base class
        Args
           *arg (any)
           **kwargs(dict): key-value pairs
        '''
        self.id = str(uuid.uuid())
        self.creation = datetime.today()
        self.update = dateitm.today()
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
        '''update current time'''
        self.update = datetime.today()
        models.storage.save()

    def to_dict(self):
        ''' return dictionary representation of instance '''
        my_dict = self.__dict__.copy()
        my_dict['creation'] = self.creation.isoformat()
        my_dict['update'] = self.update.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
