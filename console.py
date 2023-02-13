#!/usr/bin/python3
import cmd
import sys, os

file = sys.path.append("../models")
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
        lines = BaseModel()
        print(lines.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
