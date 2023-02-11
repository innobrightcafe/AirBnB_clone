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
        pass

    def new(self, obj):
        pass

    def save(self):
        pass

    def reload(self):
        pass