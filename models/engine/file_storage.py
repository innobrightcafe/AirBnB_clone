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
        self.__objects[key] = obj.to_dict()

    def save(self):
        new_dict = {}
        for item, value in self.__objects.items():
            new_dict[item] = value
        file = json.dumps(new_dict, indent=4)
        with open(self.__file_path, "w") as json_file:
            json_file.write(file)

    def reload(self):
        try:
            pass
            # with open(self.__file_path, "r") as json_file:
            #     self.__objects = json.load(json_file)
        except FileNotFoundError:
            pass