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
        self.assertEqual(str(test_base), f"[BaseModel] ({test_base.id}) {test_base.__dict__}")
'''
    def test_to_dict(self):
        test_base = BaseModel()
        self.assertEqual()
'''

if __name__ == "__main__":
    unittest.main()
