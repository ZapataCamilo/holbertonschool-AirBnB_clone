#!/usr/bin/python3
'''Testing file_storage.py'''
import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
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

    def test_new(self):
        '''Testing new mwthod'''
        storage = FileStorage()
        saitama = User()
        saitama.id = 75342
        saitama.first_name = 'Saitama'
        saitama.last_name = 'calvo'
        storage.new(saitama)
        k = saitama.__class__.__name__ + '.' + str(saitama.id)
        self.assertIsNotNone(all_data[k])

    

if __name__ == "__main__":
    unittest.main()