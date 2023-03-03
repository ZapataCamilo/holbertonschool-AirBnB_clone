#!/usr/bin/python3
'''Testing file_storage.py'''
import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
all_data = storage.all()


class TestFileStorage(unittest.TestCase):
    '''Testing FileStorage'''
    def test_all(self):
        '''Testing all method'''
        storage = FileStorage()
        self.assertIsNotNone(all_data)
        self.assertEqual(dict, type(all_data))
        self.assertIs(all_data, storage._FileStorage__objects)

if __name__ == "__main__":
    unittest.main()