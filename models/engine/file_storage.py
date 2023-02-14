#!/user/bin/python3

"""The class serializes instances to a JSON file and deserializes JSON file to instances"""

import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = type(obj).__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        file = json.dumps(self.__objects, indent=4)
        with open(self.__file_path, "w") as json_file:
            json_file.write(file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as json_file:
                self.__objects = json.load(json_file)
        except FileNotFoundError:
            pass