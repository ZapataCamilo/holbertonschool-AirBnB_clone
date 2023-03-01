'''Python AirBnB Console Project'''
import json



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
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(self.__objects, f)
