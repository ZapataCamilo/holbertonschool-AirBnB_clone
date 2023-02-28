#!/usr/bin/python3
'''Testing base_model.py'''
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''testing BaseModel'''
    def test_init(self):
        '''testing instances'''
        test_base = BaseModel()
        self.assertEqual(test_base.id, 731082)

if __name__ == "__main__":
    unittest.main()
