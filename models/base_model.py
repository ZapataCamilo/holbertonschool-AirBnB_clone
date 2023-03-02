#!/usr/bin/python3
'''Python AirBnB Console Project'''
import uuid
from datetime import datetime


class BaseModel():
    '''Defines all common attributes/methods for other classes'''

    def __init__(self, *args, **kwargs):
        '''from models import storage'''
        if kwargs:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                if k == 'created_at' or k == 'updated_at':
                    self.created_at = datetime.strptime(v,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            '''storage.new(self)'''

    def __str__(self):
        '''Print a string with Class data'''
        name = type(self).__name__
        dict = self.__dict__
        return f"[{name}] ({self.id}) {dict}"

    def save(self):
        '''Updates the public instance attribute'''
        '''from models import storage'''
        self.updated_at = datetime.now()
        '''storage.save()'''

    def to_dict(self):
        '''returns a dictionary containing all\
         keys/values of __dict__ of the instance'''
        return {"id": self.id,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat(),
                "__class__": type(self).__name__
                }
