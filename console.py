#!/usr/bin/python3
""" console """


import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'User': User,
            'State': State, 'City': City,
            'Place': Place, 'Review': Review,
            'Amenity': Amenity}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print('')
        exit()

    def emptyline(self):
        pass

    def do_create(self, arg):
        """create command to exit the program"""
        if not arg:
            print("** class name missing **")
        var = None
        if arg:
            separate_arg = arg.split()
            if len(separate_arg) == 1:
                if arg in self.classes.keys():
                    var = self.classes[arg]()
                    var.save()
                    print(var.id)
                else:
                    print("** class doesn't exist **")

    def do_show(self, arg):
        """show command to exit the program"""
        if not arg:
            print("** class name missing **")
            return
        elif arg.split()[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg.split()) > 1:
            var = arg.split()[0] + '.' + arg.split()[1]
            if var in storage.all():
                value = storage.all()
                print(value[var])
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """destroy command to exit the program"""
        if not arg:
            print("** class name missing **")
            return
        separate_arg = arg.split()
        try:
            var = eval(separate_arg[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(separate_arg) == 1:
            print("** instance id missing **")
            return
        elif len(separate_arg) > 1:
            var = separate_arg[0] + '.' + separate_arg[1]
            if var in storage.all():
                storage.all().pop(var)
                storage.save()
            else:
                print("** no instance found **")
                return

    def do_all(self, arg):
        if not arg:
            print([str(var) for var in storage.all().values()])
        elif arg not in self.clas:
            print("** class doesn't exist **")
        else:
            print([str(i) for j, i in storage.all().items() if arg in j])

    def do_update(self, arg):
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in self.clas:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        else:
            var = arg[0] + '.' + arg[1]
            if var in storage.all():
                if len(arg) > 2:
                    if len(arg) == 3:
                        print("** value missing **")
                    else:
                        setattr(storage.all()[var], arg[2], arg[3][1:-1])
                        storage.all()[var].save()
                else:
                    print("** attribute name missing **")
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
