#!/usr/bin/python3
'''Python AirBnB Console Project'''
from models.base_model import BaseModel


class User(BaseModel):
    '''inherits from BaseModel'''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
