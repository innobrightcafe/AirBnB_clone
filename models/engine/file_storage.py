<<<<<<< HEAD
#!/user/bin/python3

"""The class serializes instances to a JSON file and deserializes JSON file to instances"""

import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = type(obj).__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(FileStorage.__objects, json_file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as json_file:
                FileStorage.__objects = json.load(json_file)
        except FileNotFoundError:
            pass

=======
#!/usr/bin/python3

"""import modules"""
import json
import os

"A class FileStorage created"
class FileStorage:
    current_dir = os.getcwd()
    folder = "engine"
    __path = os.path.join(current_dir, folder)
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.id] = obj

    def save(self):
        if os.path.exits(self.__path):
            with open(self.__path + "/file.json", "a") as file:
                files = json.dumps(self.__objects, indent=4)
                file.write(files)

    def reload(self):
        pass
>>>>>>> 426ad2741d03551679e761ee1728a056e729f72b
