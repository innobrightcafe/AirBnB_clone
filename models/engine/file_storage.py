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