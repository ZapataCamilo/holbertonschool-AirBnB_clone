#!/usr/bin/python3
'''Python AirBnB Console Project'''
import uuid
import datetime
import models


class BaseModel():
    '''Defines all common attributes/methods for other classes'''
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime()
        self.updated_at = datetime.datetime()
    
    def __str__(self):
        '''Print a string with Class data'''
        name = type(self).__name__
        dict = self.__dict__
        return f"[{name}] ({self.id}) {dict}"

    def save(self):
        '''Updates the public instance attribute'''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' returns a dictionary containing all\
         keys/values of __dict__ of the instance'''
        dict_cpy = self.__dict__.copy()
        dict_cpy["created_add"] = self.created_at.isoformat()
        dict_cpy["updated_add"] = self.updated_at.isoformat()
        dict_cpy["__class__"] = type(self).__name__
        return dict_cpy
