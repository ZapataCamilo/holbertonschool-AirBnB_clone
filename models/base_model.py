#!/usr/bin/python3
'''Python AirBnB Console Project'''
import uuid
import datetime
import models


class BaseModel():
    '''Defines all common attributes/methods for other classes'''
    def __init__(self, *args):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime(year=2023, month=2, day=27, hour=16, minute=26, tzinfo=None)
        self.updated_at = datetime.datetime(year=2023, month=2, day=27, hour=16, minute=26, tzinfo=None)

    def __str__(self):
        '''Print a string with Class data'''
        name = type(self).__name__
        dict = self.__dict__
        return f"[{name}] ({self.id}) {dict}"

    def save(self):
        '''Updates the public instance attribute'''
        self.updated_at = datetime.time()

    def to_dict(self):
        ''' returns a dictionary containing all\
         keys/values of __dict__ of the instance'''
        dict_cpy = self.__dict__.copy()
        dict_cpy["created_add"] = self.created_at.isoformat()
        dict_cpy["updated_add"] = self.updated_at.isoformat()
        dict_cpy["__class__"] = type(self).__name__
        return dict_cpy
