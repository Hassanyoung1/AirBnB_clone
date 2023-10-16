#!/usr/bin/python3
"""
This module implements a simple command-line
interpreter for manipulating AirBnB data.

Major commands available:
- create: creates a new instance of a specified
 class and saves it to JSON.

- show: prints the string representation of an
instance based on class name and id.

- destroy: deletes an instance based on class name and id.

- all: prints string representations of all instances
or instances of a specified class.

- update: updates an instance based on class
name and id by adding or updating attributes.

Usage:
    Run the program: python3 console.py
"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand: (class) - command interpreter to manipulate AirBnB data
    """

    intro = "A command interpreter to manipulate AirBnB data"
    prompt = '(hbnb) '

    objects = {
        'BaseModel': BaseModel, 'User': User, 'State': State,
        'City': City, 'Amenity': Amenity, 'Place': Place, 'Review': Review
    }

    def do_quit(self, args):
        """Quit command to exit the program """
        return True

    def do_EOF(self, args):
        """Exit the program"""
        print()
        return True

    def emptyline(self):
        """Called when an empty line is entered."""
        pass

    def do_create(self, args):
        """
            Create a new instance of a class, save
            it (to the JSON file), and print its id.
        """
        if not args:
            print("** class name missing **")
        elif args in HBNBCommand.objects:
            instance = HBNBCommand.objects[args]()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
            Print the string representation of an instance
            based on the class name and id.
        """
        if not args:
            print("** class name missing **")
        else:
            arg_list = args.split()
            if arg_list[0] not in HBNBCommand.objects:
                print("** class doesn't exist **")
            elif len(arg_list) < 2:
                print("** instance id missing **")
            else:
                obj_id = "{}.{}".format(arg_list[0], arg_list[1])
                all_objs = storage.all()
                obj = all_objs.get(obj_id)
                if obj:
                    print(obj)
                else:
                    print("** no instance found **")

    def do_destroy(self, args):
        """Delete an instance based on the class name and id."""
        if not args:
            print("** class name missing **")
        else:
            arg_list = args.split()
            if arg_list[0] not in HBNBCommand.objects:
                print("** class doesn't exist **")
            elif len(arg_list) < 2:
                print("** instance id missing **")
            else:
                obj_id = "{}.{}".format(arg_list[0], arg_list[1])
                all_objs = storage.all()
                obj = all_objs.get(obj_id)
                if obj:
                    del all_objs[obj_id]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, args):
        """
            Print all string representations of instances,
            or instances of a specified class.
        """
        if not args:
            print([str(obj) for obj in storage.all().values()])
        elif args in HBNBCommand.objects:
            print([str(obj) for obj in storage.all().values()
                  if isinstance(obj, HBNBCommand.objects[args])])
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
            Update an instance based on the class name and
            id by adding or updating attributes.
        """
        if not args:
            print("** class name missing **")
        else:
            arg_list = args.split()
            if arg_list[0] not in HBNBCommand.objects:
                print("** class doesn't exist **")
            elif len(arg_list) < 2:
                print("** instance id missing **")
            elif len(arg_list) < 3:
                print("** attribute name missing **")
            elif len(arg_list) < 4:
                print("** value missing **")
            else:
                obj_id = "{}.{}".format(arg_list[0], arg_list[1])
                all_objs = storage.all()
                obj = all_objs.get(obj_id)
                if obj:
                    setattr(obj, arg_list[2], eval(arg_list[3]))
                    obj.save()
                else:
                    print("** no instance found **")

    def default(self, args):
        """Method called when the command prefix is not recognized."""
        tokens = args.split('.')
        if len(tokens) == 2 and \
            tokens[0] in HBNBCommand.objects and \
                tokens[1] == "all()":
            self.do_all(tokens[0])
        else:
            print("** command not found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
