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
        file = json.dumps(FileStorage.__objects, indent=4)
        with open(FileStorage.__file_path, "w") as json_file:
            json_file.write(file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as json_file:
                FileStorage.__objects = json.load(json_file)
        except FileNotFoundError:
            pass