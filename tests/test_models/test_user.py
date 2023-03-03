#!/usr/bin/python3
'''Testing user.py'''
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    '''Testing User'''
    def test_email(self):
        '''Testing email attribute'''
        saitama = 