#!/usr/bin/python3
'''Testing file_storage.py'''
import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models import storage
all_data = storage.all()


class TestFileStorage(unittest.TestCase):
    '''Testing FileStorage'''
    def setUp(self):
        '''setting instances'''
        self.test_base = BaseModel()
        self.test_user = User()
        self.filepath = 'file.json'
        self.test_base.save()
        self.test_user.save()

    def tearDown(self):
        '''Tear down the file.json'''
        os.remove(self.filepath)

    def test_all(self):
        '''Testing all method'''
        self.assertEqual(len(all_data), 2)
        self.assertIn(f'{type(self.test_base).__name__}.{self.test_base.id}',
                          all_data)
        self.assertIn(f'{type(self.test_user).__name__}.{self.test_user.id}',
                          all_data)
        '''storage = FileStorage()
        self.assertIsNotNone(all_data)
        self.assertEqual(dict, type(all_data))
        self.assertIs(all_data, storage._TestFileStorage__objects)'''

    def test_new(self):
        '''Testing new method'''
        storage = FileStorage()
        saitama = User()
        saitama.id = 75342
        saitama.first_name = 'Saitama'
        saitama.last_name = 'calvo'
        storage.new(saitama)
        k = saitama.__class__.__name__ + '.' + str(saitama.id)
        self.assertIsNotNone(all_data[k])

    def test_save(self):
        '''Testing save method'''
        storage = FileStorage()
        '''storage.save()
        exist = os.path.exists('file.json')
        self.assertTrue(exist)'''
        with self.assertRaises(TypeError):
            storage.save(123)

    def test_reload(self):
        '''Testing reload method'''
        for all_id in all_data.keys():
            obj = all_data[all_id]
        print(obj)
        self.assertIsNotNone(obj)
        '''with self.assertRaises(TypeError):
            storage.reload(123)'''


if __name__ == "__main__":
    unittest.main()