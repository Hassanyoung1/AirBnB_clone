#!/usr/bin/python3
"""
The console program: This program creates simple command line interpreters
used in handling/operating the AirBnB site.

Major commands to be used are: create, update, and destroy, which will
handle the data creation, update, and destruction of data not needed.
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
    Entry point of the command interpreter.
    """

    prompt = '(hbnb) '

    objects = {'BaseModel': BaseModel, 'User': User,
               'State': State, 'City': City,
               'Amenity': Amenity, 'Place': Place,
               'Review': Review
               }

    def do_quit(self, args):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, args):
        """
        EOF command to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        Called when an empty line is entered in response to the prompt.
        """
        pass

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel

        Return:
            The id of the instance.
        """
        if args == '':
            print("** class name missing **")
        elif args in HBNBCommand.objects.keys():
            my_model = HBNBCommand.objects[args]()
            my_model.save()
            print(my_model.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the
        class name and id. Ex: $ show BaseModel 1234-1234-1234

        Return:
            The string representation of the object id.
        """
        token = args.split()
        if args == "":
            print("** class name missing **")
        elif token[0] in HBNBCommand.objects.keys():
            if len(token) < 2:
                print("** instance id missing **")
                return False
            all_objs = storage.all()
            obj_id = '{}.{}'.format(token[0], token[1])
            if obj_id not in all_objs.keys():
                print("** no instance found **")
            else:
                print(all_objs[obj_id])
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234

        Return:
            Nothing.
        """
        token = args.split()
        if args == "":
            print("** class name missing **")
        elif token[0] in HBNBCommand.objects.keys():
            if len(token) < 2:
                print("** instance id missing **")
                return False
            all_objs = storage.all()
            obj_id = '{}.{}'.format(token[0], token[1])
            if obj_id not in all_objs.keys():
                print("** no instance found **")
            else:
                del all_objs[obj_id]
                storage.save()
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """
        Prints all string representation of all instances based or not
        on the class name. Ex: $ all BaseModel or $ all.

        Return:
            (list) The printed result must be a list of strings.
        """
        token = args.split()
        if args == "" or token[0] in HBNBCommand.objects.keys():
            all_objs = storage.all()
            str_rep = [(str(all_objs[obj_id])) for obj_id in all_objs.keys()]
            print(str_rep)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        token = args.split()
        if args == "":
            print("** class name missing **")
        elif token[0] in HBNBCommand.objects.keys():
            if len(token) < 2:
                print("** instance id missing **")
                return False
            all_objs = storage.all()
            obj_id = '{}.{}'.format(token[0], token[1])
            if obj_id not in all_objs.keys():
                print("** no instance found **")
            else:
                if len(token) < 3:
                    print("** attribute name missing **")
                    return False
                elif len(token) < 4:
                    print("** value missing **")
                    return False
                if token[3].startswith('"') and token[3].endswith('"'):
                    token[3] = token[3][1:-1]
                key = '{}.{}'.format(token[0], token[1])
                setattr(all_objs[key], token[2], token[3])
                storage.save()
        else:
            print("** class doesn't exist **")

    def default(self, args):
        """
        Method called on an input line when the command prefix is not
        recognized.
        """
        token = args.split('.')
        if token[0] in HBNBCommand.objects.keys():
            if len(token) != 2:
                return
            cmd_id = token[1].strip(')').split('(')
            cmdd = cmd_id[0]
            if token[1] == "all()":
                str_rep = []
                all_objs = storage.all()
                for obj_id in all_objs.keys():
                    obj = obj_id.split('.')[0]
                    if obj == token[0]:
                        str_rep.append(str(all_objs[obj_id]))
                print(str_rep)
            elif token[1] == "count()":
                count = 0
                all_objs = storage.all()
                for obj_id in all_objs.keys():
                    obj = obj_id.split('.')[0]
                    if obj == token[0]:
                        count = count + 1
                print(count)
            elif cmdd == "show":
                if len(cmd_id) < 2:
                    print("** instance id missing **")
                else:
                    id = cmd_id[1][1:-1]
                    obj_id = '{} {}'.format(token[0], id)
                    self.do_show(obj_id)
            elif cmdd == "destroy":
                if len(cmd_id) < 2:
                    print("** instance id missing **")
                else:
                    id = cmd_id[1][1:-1]
                    obj_id = '{} {}'.format(token[0], id)
                    self.do_destroy(obj_id)
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
