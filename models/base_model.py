#!/usr/bin/python3

"""import modules"""
import uuid
import datetime
import time

"""create a class Base"""
class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.name = None
        self.my_number = None
        self.created_at = datetime.datetime.now()
        self.updated_at = None
        self.dict = {}
    
    def __str__(self):
        return f"{type(self.id)} {self.id} {self.dict}"
    
    def save(self):
        self.updated_at = datetime.datetime.now()
    
    def to_dict(self):
        self.dict["my_number"] = self.my_number
        self.dict["name"] = self.name
        self.dict["updated_at"] = self.updated_at
        self.dict["id"] = self.id
        self.dict["created_at"] = self.created_at
        return self.dict


for user in range(1):
    user = BaseModel()
    user.name = "My First Model"
    user.my_number = 89
    x = user.to_dict()
    print(user)
    print("======================================================")
    print(x)
    print("======================================================")
