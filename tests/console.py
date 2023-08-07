#!/usr/bin/python3
""" BackEnd Interpreter for HBnB console. """
import re
import cmd
import sys
from shlex import split
from models import storage
from models.base_model import BaseModel


def tokenize(line):
    """ tokenize : converts the line into tuples and last
    element is always the full line"""
    return [i.strip(",") for i in split(line)]


class HBNBCommand(cmd.Cmd):
    """ Configures the command Interpreter for Holberton app """
    prompt = "(hbnb) "
    __classes = [
            "BaseModel",
            "User"]
    # intro = 'Simple Command Interpreter for the holberton Web app'

    def do_EOF(self, arg):
        """ End of File """
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program.\n"""
        return True

    def emptyline(self):
        """ Empty line triggered """
        pass

    def do_create(self, arg):
        """ create an object class with an id """
        args = tokenize(arg)
        print(args)
        if len(args) == 0:
            print("** class name missing **")
        else:
            if not args[0] in self.__classes:
                print("** class doesn't exist **")
            else:
                print(eval(args[0])().id)
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
