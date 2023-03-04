import cmd
import linecache
from os import name
from binhex import LINELEN
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. 
        Usage: create <class name>
        """
        if not line:
            print("** class name missing **")
            return

        class_name = line.strip()
        if class_name not in models.all_models:
            print("** class doesn't exist **")
            return

        new_instance = models.all_models[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        if not line:
            print("** class name missing **")
            return

        line = line.strip().split()
        if len(line) < 2:
            print("** instance id missing **")
            return

        class_name, instance_id = line[0], line[1]
        if class_name not in models.all_models:
            print("** class doesn't exist **")
            return

        instances = models.storage.all(models.all_models[class_name])
        if instance_id not in instances:
            print("** no instance found **")
            return

        print(instances[instance_id])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change into the JSON file).
        Usage: destroy <class name> <id>
        """
        if not line:
            print("** class name missing **")
            return

        line = line.strip().split()
        if len(line) < 2:
            print("** instance id missing **")
            return

        class_name, instance_id = line[0], line[1]
        if class_name not in models.all_models:
            print("** class doesn't exist **")
            return

        instances = models.storage.all(models.all_models[class_name])
        if instance_id not in instances:
            print("** no instance found **")
            return

        instances[instance_id].delete()
        models.storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name.
        Usage: all <class name>
        """
        class_name = line.strip() if line else None
        if class_name and class_name not in models.all_models:
            print("** class doesn't exist **")
            return

        instances = models.storage.all(models.all_models[class_name] if class_name else BaseModel)
        print([str(instances[instance_id]) for instance_id in instances])

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file
        Usage: update <class name> <id> <attribute name> "<attribute value>"""
    if not linecache:
        print("** class name missing **")
        return

    line = LINELEN.strip().split()
    if len(line) < 2:
        print("** instance id missing **")
        return

    if len(line) < 3:
        print("** attribute name missing **")
        return

    if len(line) < 4:
        print("** value missing **")
        return

    class_name, instance_id, attr_name, attr_value = line[0], line[1], line[2], ' '.join(line[3:])

    if class_name not in models.all_models:
        print("** class doesn't exist **")
        return

    instances = models.storage.all(models.all_models[class_name])
    if instance_id not in instances:
        print("** no instance found **")
        return

    instance = instances[instance_id]
    setattr(instance, attr_name, eval(attr_value))
    instance.save()

    """ Usage: update <class name> <id> <attribute name> "<attribute value>"
    """
    if not line:
        print("** class name missing **")
        return
    line = line.strip().split()
    if len(line) < 2:
        print("** instance id missing **")
        return
    if len(line) < 3:
        print("** attribute name missing **")
        return
    if len(line) < 4:
        print("** value missing **")
        return

    class_name, instance_id, attr_name, attr_value = line[0], line[1], line[2], ' '.join(line[3:])
    if class_name not in models.all_models:
        print("** class doesn't exist **")
        return

    instances = models.storage.all(models.all_models[class_name])
    if instance_id not in instances:
        print("** no instance found **")
        return

    setattr(instances[instance_id], attr_name, attr_value)
    instances[instance_id].save()

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt.
        Does nothing.
        """
        pass
    if name == 'main':
    HBNBCommand().cmdloop()