#!/usr/bin/python3

"""import modules"""
import uuid
import datetime
import time

"""create a class Base"""
class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = None
    
    def __str__(self):
        return f"{type(self.id)} {self.id} {self.__dict__}"
    
    def save(self):
        self.updated_at = datetime.datetime.now()
    
    def to_dict(self):
        pass


for user in range(6):
    user = BaseModel()
    print(user.id)
    user.save()
    print(user)
    print("=================")
