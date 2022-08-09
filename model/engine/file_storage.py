#!/usr/bin/python3

import json
import models


class FileStorage:
    
    # path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    @classmethod
    def clear(cls):
        FileStorage.__objects = {}

    def all(self):
    
        return self.__objects

    def new(self, obj):
       
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
    
        json_objects = {}
        for key, value in self.__objects.items():
            json_objects[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
    
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
                for key in jo:
                    self.__objects[key] = getattr(
                        models, jo[key]['__class__'])(**jo[key])
        except Exception:
            pass
