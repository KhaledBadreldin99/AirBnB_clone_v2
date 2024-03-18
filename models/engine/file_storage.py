#!/usr/bin/python3
import os.path
import os
import json

"""
The module file_storage includes a class named FileStorage,
which handles the serialization of instances to a JSON file
and the deserialization ofJSON files back into instances.
"""

class FilelStorage():
    """
    This class is responsible for converting instances into
    a JSON file and converting JSON files back into instances.
    """
    ''' initializing values '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' returns the dictionary __objects '''
        if cls in not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>,id '''
        if obj:
            ''' adds the object and the key to __objects id the obj exists '''
            name = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[name] = obj

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path) '''
        my_dict = {}

        for keys, val in self.__objects.items():
            ''' serializes each object using the key '''
            my_dict[keys] = val.to_dict()

        with open(self.__file_path, "w") as my_file:
            json.dump(my_dict, my_file)

    def reload(self):
        ''' deserializes/loads the JSON file to __objects '''

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        my_dict = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
            }
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r") as file_path:
            objects = json.load(file_path)
            self.__objects = {}
            for key in objects:
                name = key.split(".")[0]
                self.__objects[key] = my_dict[name](**objects[key])

    def delete(self, obj=None):
        """Remove the pbject from the __objects if it exists within it."""
        if obj is not None:
            obj_key = obj.to_dict()['__class__'] + '.' + obj.id
            if obj_key in self.__objects.keys():
                delf self.__objects[obj_key]

    def close(self):
        """Invoke the reload() function to deserialize the JSON file into objects."""
        self.reload()
