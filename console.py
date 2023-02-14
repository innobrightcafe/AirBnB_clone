#!/usr/bin/python3
import cmd
import sys
import os

dir = os.getcwd()
folder1 = "engine"
folder2 = "models"
_path1 = os.path.join(dir, folder1)
_path2 = os.path.join(dir, folder2)

"""Include path to python system environment"""
sys.path.append(_path1)
sys.path.append(_path2)

from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Simple command processor."""
    intro = "welcome to the console"
    prompt = "(hbnb)"
    x = "Quit command to exit the program"

    def do_EOF(self, line):
        return True

    def do_help(self, line):
        if line:
            if line == "quit":
                value = getattr(self, 'x')
                print(value)
        else:
            names = self.get_names()
            commands = [name[3:] for name in names if name.startswith('do_')]
            print("Documented commands (type help <topic>")
            print("=========================================")
            print("%s" % '  '.join(commands))

    def do_quit(self, line):
        return True

    def do_create(self, line):
        """create a new instance of basemodel"""
        if line == "BaseModel":
            lines = BaseModel()
            lines.save()
            print(lines.id)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
