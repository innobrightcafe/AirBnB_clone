#!/usr/bin/python3

"""import modules"""
import uuid
import datetime

from __init__ import storage

"""create a class BaseModel"""

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.data = kwargs
        self.my_number = ""
        self.name = ""
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.datetime.now())
        self.updated_at = ""

        found = False
        for item in storage.all():
            if item == self.__dict__:
                found = True
                break
        if not found:
            storage.new(self)

    def __str__(self):
        return f"{[self.__class__.__name__]} ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = str(datetime.datetime.now())
        storage.save()

    def to_dict(self):
        self.__dict__["my_number"] = self.my_number
        self.__dict__["name"] = self.name
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["updated_at"] = self.updated_at
        self.__dict__["id"] = self.id
        self.__dict__["created_at"] = self.created_at
        return self.__dict__
