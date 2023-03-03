#!/usr/bin/python3
'''Testing file_storage.py'''
"""import unittest
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
        self.assertEqual(len(all_data), 9)
        self.assertIn(f'{type(self.test_base).__name__}.{self.test_base.id}',
                          all_data)
        self.assertIn(f'{type(self.test_user).__name__}.{self.test_user.id}',
                          all_data)

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
        with open(self.filepath, mode='r') as f:
            data = json.load(f)
            self.assertEqual(len(data), 17)
            self.assertIn(f'{type(self.test_base).__name__}.{self.test_base.id}',
                          all_data)
            self.assertIn(f'{type(self.test_user).__name__}.{self.test_user.id}',
                          all_data)

    def test_reload(self):
        '''Testing reload method'''
        for all_id in all_data.keys():
            obj = all_data[all_id]
        print(obj)
        self.assertIsNotNone(obj)
        '''with self.assertRaises(TypeError):
            storage.reload(123)'''


if __name__ == "__main__":
    unittest.main()"""

#!/usr/bin/python3
"""Unittest module for the class State
"""
import unittest
import datetime
import models
from models.engine import file_storage
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """methods of the test for class State
    """
    def test_documentation(self):
        """this checks all the documentation
        of all the methods of the class
        """
        self.assertIsNotNone(file_storage.__doc__)
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_uniqueId(self):
        """this check if the instance
        that are created has a unique id
        """
        instance1 = FileStorage()
        instance2 = FileStorage()
        self.assertNotEqual(instance1, instance2)

    def test_exec_permissions(self):
        """Method that test for check the execution permissions
        """
        read = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(write)
        exect = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(exect)

    def test_typeData(self):
        """this method check the type of
        the atributes when created a instance
        """
        instance1 = FileStorage()
        self.assertIsInstance(instance1, FileStorage)

if __name__ == '__main__':
    unittest.main()