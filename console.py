#!/usr/bin/python3
"""Import modules cmd and BaseModel class"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models import storage
from models.amenity import Amenity
from models.review import Review
from models.place import Place
"""Console for AirBnB clone"""


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "City": City,
        "State": State,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_help(self, arg):
        """Displays description of a command"""
        super().do_help(arg)

    def do_create(self, arg):
        """create command to exit the program"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            obj = self.classes[arg]()
            storage.new(obj)
            storage.save()
            print(obj.id)

    def do_show(self, arg):
        """show command to exit the program"""
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key in storage.all():
                print(storage.all()[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """destroy command to exit the program"""
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key in storage.all():
                del storage.all()[obj_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all instances of a class"""
        obj_list = []
        if arg and arg not in self.classes:
            print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                if not arg or type(obj).__name__ == arg:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, arg):
        """Updates an object with new attributes"""
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            all_obj = storage.all()
            if obj_key in all_obj:
                obj = all_obj[obj_key]
                setattr(obj, args[2], args[3])
                storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
