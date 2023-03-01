#!/usr/bin/python3
'''Python AirBnB Console Project'''
import json
from models.base_model import BaseModel



class FileStorage():
    '''Serializes instances to a JSON file and
    deserializes JSON file to instances'''
    __file_path = "file.json"
    __objects = {}
    def all(self):
        '''Returns the dictionary __objects'''
        return self.__objects
    
    def new(self, obj):
        ''' sets in __objects the obj with key
         <obj class name>.id'''
        obj_key = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[obj_key] = obj

    def save(self):
        '''Serializes __objects to the JSON file'''
        dict_data = {}
        v = BaseModel()
        for k, v in self.__objects.items():
            dict_data[k] = v.to_dict()
        with open(self.__file_path, mode="w") as f:
            json.dump(dict_data, f)

    def reload(self):
        ''''''
        if self.__file_path:
            try:
                with open(self.__file_path, mode="r") as f:
                    json.load(f)
            except FileNotFoundError:
                pass
