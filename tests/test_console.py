#!/usr/bin/python3
"""Defines unittests for console.py file

Unittest classes:
    TestHBNBCommand_prompt
    TestHBNBCommand_all
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_count
    TestHBNBCommand_update
    TestHBNBCommand_destroy
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_quit
"""

import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO

class TestHBNBCommand_prompt(unittest.TestCase):
    """Unittests for testing pf prompts of the HBNB command interpreter"""
    
    def testEmptyLine(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())
    def testPromptString(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for testing of help command messages of the HBNB command interpreter"""

    def test_help_all(self):
        help_var = ("Usage: all or all <class> or <class>.all()\n"
            "Display string representation of all the instances of a class.\n"
            "If no class is specified, displays all objects.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(help_var, output.getvalue().strip())
    def test_help_count(self):
        help_var = ("Usage: count <class> or <class>.count()\n"
                    "Get the number of instances of a class")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(help_var, output.getvalue().strip())
    def test_help_show(self):
        help_var = ("Usage: show <class> <id> or <class>.show(<id>)\n"
                    "Show the string representation of a class instance of"
                    "a given id")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(help_var, output.getvalue().strip())
    def test_help_create(self):
        help_var = ("Usage: create <class>\n"
                    "Create a new class instance and print its id")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(help_var, output.getvalue().strip())
    def test_help_update(self):
        help_var = ("Usage: update <class> <id> <attributeName> <attributeValue> or"
                    "\n <class>.update(<id>, <attributeName>, <attributeValue>)"
                    "or\n <class>.update(<id>, <dictionary>)\n"
                    "a given attribute key and value pair")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(help_var, output.getvalue().strip())
    def test_help(self):
        help_var = ("Documented commands (type help <topic>):\n"
                    "======================================\n"
                    "EOF all count create destroy quit update help show")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(help_var, output.getvalue().strip())
    def test_help_destroy(self):
        help_var = ("Usage: destroy <class> <id> or <class>.destroy(<id>)\n"
                    "Delete a class instance of a given id")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(help_var, output.getvalue().strip())
    def test_help_EOF(self):
        help_var = ("EOF (End Of File) signal to exit program")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(help_var, output.getvalue().strip())
    def test_help_quit(self):
        help_var = ("Quit command to exit the program")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(help_var, output.getvalue().strip())

class TestHBNBCommand_exit(unittest.TestCase):
    """Unittests for testing the exit command to exit from the HBNB command interpreter"""

    def test_EOF_exit(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))
    
    def test_quit_exit(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

class TestHBNBCommand_create(unittest.TestCase):
    """Unittests for testing how to create from the HBNB command interpreter"""

    @classmethod
    def set_up(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}
    
    @classmethod
    def tear_down(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
    
    def test_create_missing_class(self):
        correction = "class name missing"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create mymodel"))
            self.assertEqual(correction, output.getvalue().strip())
    
    def test_create_invalid_syntax(self):
        correction = "unknown syntax: mymodel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("mymodel.create()"))
            self.assertEqual(correction, output.getvalue().strip())
        correction = "unknown syntax: basemodel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("basemodel.create()"))
            self.assertEqual(correction, output.getvalue().strip())
    
    def test_create_object(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create basemodel"))
            self.assertLess(0, len(output.getvalue().strip()))
            testing_key = "basemodel.{}".format(output.getvalue().strip())
            self.assertIn(testing_key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(output.getvalue().strip()))
            testing_key = "User.{}".format(output.getvalue().strip())
            self.assertIn(testing_key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(output.getvalue().strip()))
            testing_key = "City.{}".format(output.getvalue().strip())
            self.assertIn(testing_key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(output.getvalue().strip()))
            testing_key = "State.{}".format(output.getvalue().strip())
            self.assertIn(testing_key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(output.getvalue().strip()))
            testing_key = "Place.{}".format(output.getvalue().strip())
            self.assertIn(testing_key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(output.getvalue().strip()))
            testing_key = "Amenity.{}".format(output.getvalue().strip())
            self.assertIn(testing_key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(output.getvalue().strip()))
            testing_key = "Review.{}".format(output.getvalue().strip())
            self.assertIn(testing_key, storage.all().keys())

class TestHBNBCommand_show(unittest.TestCase):
    """Unittests for testing how to show from the HBNB command interpreter"""

    @classmethod
    def set_up(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}
    
    @classmethod
    def tear_down(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_show_missing_class(self):
        correction = "class name missing"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(correction, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".show()"))
            self.assertEqual(correction, output.getvalue().strip())
    
    def test_create_invalid_class(self):
        correction = "class does not exist"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show mymodel"))
            self.assertEqual(correction, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("mymodel.show()"))
            self.assertEqual(correction, output.getvalue().strip())
    
    def test_show_missing_id(self):
        correction = "id missing"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show basemodel"))
            self.assertEqual(correction, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show User"))
            self.assertEqual(correction, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertEqual(correction, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertEqual(correction, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertEqual(0, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertEqual(correction, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertEqual(correction, output.getvalue().strip())

    def test_show_missing_id_dot(self):
        correction = "id missing"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("basemodel.show()"))
            self.assertEqual(correction, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.show()"))
            self.assertEqual(correction, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.show()"))
            self.assertEqual(correction, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.show()"))
            self.assertEqual(correction, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.show()"))
            self.assertEqual(0, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.show()"))
            self.assertEqual(correction, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.show()"))
            self.assertEqual(correction, output.getvalue().strip())

    def test_show_no_id_found_space(self):
        correction = "no id found"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show basemodel"))
            self.assertEqual(correction, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show User 1"))
            self.assertEqual(correction, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show City 1"))
            self.assertEqual(correction, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show State 1"))
            self.assertEqual(correction, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Place 1"))
            self.assertEqual(0, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Amenity 1"))
            self.assertEqual(correction, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Review 1"))
            self.assertEqual(correction, output.getvalue().strip())

    def test_show_no_id_found_dot(self):
        correction = "not found"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("basemodel.show(1)"))
            self.assertEqual(correction, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.show(1)"))
            self.assertEqual(correction, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.show(1)"))
            self.assertEqual(correction, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.show(1)"))
            self.assertEqual(correction, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.show(1)"))
            self.assertEqual(0, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.show(1)"))
            self.assertEqual(correction, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.show(1)"))
            self.assertEqual(correction, output.getvalue().strip())
