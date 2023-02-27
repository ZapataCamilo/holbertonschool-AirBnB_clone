#!/usr/bin/python3
'''Python AirBnB Console Project'''
import uuid
import datetime


class BaseModel():
    '''Defines all common attributes/methods for other classes'''
    date = datetime.datetime(year=2023, month=2, day=27, hour=16, minute=26, tzinfo=None)

    def __init__(self, *args):
        self.id = str(uuid.uuid4())
        self.created_at = BaseModel.date
        self.updated_at = BaseModel.date
    def __str__(self):
        '''Print a string with Class data'''
        name = type(self).__name__
        dict = self.__dict__
        return f"[{name}] ({self.id}) {dict}"

    def save(self):
        '''Updates the public instance attribute'''
        self.updated_at = BaseModel.date
    def to_dict(self):
        ''' returns a dictionary containing all\
         keys/values of __dict__ of the instance'''
        return {"id": str(uuid.uuid4()),
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat(),
                "__class__": type(self).__name__
                }
