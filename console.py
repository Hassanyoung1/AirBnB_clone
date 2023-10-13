#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage 

class HBNBCommand(cmd.Cmd):
    """ entry point of the command interpret"""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """ Quit the program"""
        return True 
    
    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True
    
    def do_emptyline(self):
        """ program is an emptyline """
        pass 
    def do_create(self, args):
        if args == "BaseModel":
           models = BaseModel()
           models.save()
           print(models.id)
        elif args == "":
           print("** class name missing **")
        elif args != "BaseModel":
           print("** class doesn't exist **")
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()



    

