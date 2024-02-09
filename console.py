#!/usr/bin/python3
"""Defines the AirBnB clone console"""
import cmd
import re
from shlex import split
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

def parse(arg):
    curlyBraces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curlyBraces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            tokenizeInputs = split(arg[:brackets.span()[0]])
            returnList = [i.strip(",") for i in tokenizeInputs]
            returnList.append(brackets.group())
            return returnList
    else:
        tokenizeInputs = split(arg[:curlyBraces.span()[0]])
        returnList = [i.strip(",") for i in tokenizeInputs]
        returnList.append(curlyBraces.group())
        return returnList
class HBNBCommand(cmd.Cmd):
    """Defines AirBnB command interpreter for the console
    
        Arg:
            prompt(string): command prompt being parsed
    """

    prompt = "(hbnb) "
    classes = {"BaseModel", "User", "State", "City", "Place", "Amenity", "Review"}

    def emptyline(self):
       """Nothing should be done if an empty file is parsed"""
       pass

    def default(self, arg):
        """Default behavior when input is invalid"""
        commandMapping = {
            "all": self._all, "create": self._create, "update": self._update, "show": self._show, "count": self._count, "destroy": self._destroy
        }
        mapMatching = re.search(r"\.", arg)
        if mapMatching is not None:
            argList = [arg[:mapMatching.span()[0]], arg[mapMatching.span()[1]:]]
            mapMatching = re.search(r"\((.*?)\)", argList[1])
            if mapMatching is not None:
                command = [argList[1][:mapMatching.span()[0]], mapMatching.group()[1:-1]]
                if command[0] in commandMapping.keys():
                    call = "{} {}".format(argList[0], command[1])
                    return commandMapping[commandMapping[0]](call)
        print("*** Invalid Syntax: {}. Try again.".format(arg))
        return False
    
    def _EOF(self, arg):
        """End Of File(EOF) signal"""
        print("")
        return True
   
    def _quit(self, arg):
        """Quit command"""
        return True
    
    def _create(self, arg):
        """ Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        argList = parse(arg)
        if len(argList) == 0:
            print("Class Name is missing")
        elif argList[0] not in HBNBCommand.classes:
            print("Class does not exist")
        else:
            print(eval(argList[0])().id)
            FileStorage.save()

    def _all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""

        argList = parse(arg)
        if len(argList) > 0 and argList[0] not in HBNBCommand.classes:
            print("Class does not exist")
        else:
            objectList = []
            for obj in FileStorage.all().values():
                if len(argList) > 0 and argList[0] == obj.__class__.__name__:
                    objectList.append(obj.__str__())
                elif len(argList) == 0:
                    objectList.append(obj.__str__())
            print(objectList)
    def _update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)"""
        argList = parse(arg)
        objectDict = FileStorage.all()
        if len(argList) == 0:
            print("Class name is missing")
            return False
        if argList[0] not in HBNBCommand.classes:
            print("Class does not exist")
            return False
        if len(argList) == 1:
            print("Instance id is missing")
            return False
        if "{}.{}".format(argList[0],argList[1]) not in objectDict.keys():
            print("No instance found")
            return False
        if len(argList) == 2:
            print("Attribute name is missing")
            return False
        if len(argList) == 3:
            try:
                type(eval(argList[2])) != dict
            except NameError:
                print("Value is missing")
                return False
        if len(argList) == 4:
            obj = objectDict["{}.{}".format(argList[0], argList[1])]
            if argList[2] in obj.__class__.__dict__.keys():
                valueType = type(obj.__class__.__dict__[argList[2]])
                obj.__dict__[argList[2]] = valueType(argList[3])
            else:
                obj.__dict__[argList[2]] = argList[3]
        elif type(eval(argList[2])) == dict:
            obj = objectDict["{}.{}".format(argList[0], argList[1])]
            for key , value in eval(argList[2]).items():
                if (key in obj.__class__.__dict__.keys() and type(obj.__class__.__dict__[key]) in {str, int, float}):
                    valueType = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = valueType(value)
                else:
                    obj.__dict__[key] = value
        FileStorage.save()
    def _show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        argList = parse(arg)
        objectDict = FileStorage.all()
        if len(argList) == 0:
            print("Class name is missing")
        elif argList[0] not in HBNBCommand.classes:
            print("Class does not exist")
        elif len(argList) == 1:
            print("Instance id is missing")
        elif "{}.{}".format(argList[0], argList[1]) not in objectDict:
            print("No instance is found")
        else:
            print(objectDict["{}.{}".format(argList[0], argList[1])])
    def _count(self, arg):
        """Get the number of instances of a class"""
        argList = parse(arg)
        counter = 0
        for obj in FileStorage.all().values():
            if argList[0] == obj.__class__.__name__:
                counter += 1
        print(counter)
    def _destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        argList = parse(arg)
        objectDict = FileStorage.all()
        if len(argList) == 0:
            print("Class name is missing")
        elif argList[0] not in HBNBCommand.classes:
            print("Class does not exist")
        elif len(argList) == 1:
            print("Instance id is missing")
        elif "{}.{}".format(argList[0], argList[1]) not in objectDict.keys():
            print("No Instance Found")
        else:
            del objectDict["{}.{}".format(argList[0], argList[1])]
            FileStorage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
