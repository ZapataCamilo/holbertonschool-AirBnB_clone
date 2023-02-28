#!/usr/bin/python3
'''Testing base_model.py'''
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''testing BaseModel'''
    def test_init(self):
        '''testing instances'''
        test_base = BaseModel()
        self.assertEqual(str, type(test_base.id))
        self.assertEqual(datetime.datetime, type(test_base.created_at))
        self.assertEqual(datetime.datetime, type(test_base.updated_at))

    def test_str(self):
        '''Testing __str__ method'''
        test_base = BaseModel()
        self.assertEqual(type(str(test_base)), str)

if __name__ == "__main__":
    unittest.main()
