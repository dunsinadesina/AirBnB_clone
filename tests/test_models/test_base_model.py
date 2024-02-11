#!/usr/bin/python3
"""Defines unittests for models/base_model.py file

Unittest classes:
    TestBaseModelInstant
    TestBaseModelSave
    TestBaseModelDict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModelInstant(unittest.TestCase):
    """Unittests for testing instantiation of the class BaseModel"""

    def test_no_arg_instant(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objs(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_string(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        basemodel1 = BaseModel()
        basemodel2 = BaseModel()
        self.assertNotEqual(basemodel1.id, basemodel2.id)

    def test_two_models_created_at(self):
        basemodel1 = BaseModel()
        sleep(0.05)
        basemodel2 = BaseModel()
        self.assertLess(basemodel1.created_at, basemodel2.created_at)

    def test_two_models_updated_at(self):
        basemodel1 = BaseModel()
        sleep(0.05)
        basemodel2 = BaseModel()
        self.assertLess(basemodel1.updated_at, basemodel2.updated_at)

    def test_str_representation(self):
        date_t = datetime.today()
        date_t_repr = repr(date_t)
        basemodel = BaseModel()
        basemodel.id = "123456"
        basemodel.created_at = basemodel.updated_at = date_t
        basemodelString = basemodel.__str__()
        self.assertIn("[BaseModel] (123456)", basemodelString)
        self.assertIn("'id': '123456'", basemodelString)
        self.assertIn("'created_at': " + date_t_repr, basemodelString)
        self.assertIn("'updated_at': " + date_t_repr, basemodelString)

    def test_arg_unused(self):
        basemodel = BaseModel(None)
        self.assertNotIn(None, basemodel.__dict__.values())

    def test_instantiation_with_kwargs(self):
        date_t = datetime.today()
        d_t_iso = d_t.isoformat()
        bmodel = BaseModel(id="345", created_at=d_t_iso, updated_at=d_t_iso)
        self.assertEqual(basemodel.id, "345")
        self.assertEqual(basemodel.created_at, date_t)
        self.assertEqual(basemodel.updated_at, date_t)

    def test_instante_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instante_with_args_and_kwargs(self):
        date_t = datetime.today()
        d_t_iso = d_t.isoformat()
        bmd = BaseModel("12", id="345", created_at=d_t_iso, updated_at=d_t_iso)
        self.assertEqual(bmd.id, "345")
        self.assertEqual(bmd.created_at, date_t)
        self.assertEqual(bmd.updated_at, date_t)


class TestBaseModelSave(unittest.TestCase):
    """Unittests for testing save method of the class BaseModel"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        basemodel = BaseModel()
        sleep(0.05)
        first_updated_at = basemodel.updated_at
        basemodel.save()
        self.assertLess(first_updated_at, basemodel.updated_at)

    def test_two_saves(self):
        basemodel = BaseModel()
        sleep(0.05)
        first_updated_at = basemodel.updated_at
        basemodel.save()
        second_updated_at = basemodel.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        basemodel.save()
        self.assertLess(second_updated_at, basemodel.updated_at)

    def test_save_with_arg(self):
        basemodel = BaseModel()
        with self.assertRaises(TypeError):
            basemodel.save(None)

    def test_save_updates_file(self):
        basemodel = BaseModel()
        basemodel.save()
        bmid = "BaseModel." + basemodel.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


class TestBaseModelDict(unittest.TestCase):
    """Unittests for testing to_dict method of the class BaseModel"""

    def test_to_dict_type(self):
        basemodel = BaseModel()
        self.assertTrue(dict, type(basemodel.to_dict()))

    def test_to_dicts_correct_keys(self):
        basemodel = BaseModel()
        self.assertIn("id", basemodel.to_dict())
        self.assertIn("created_at", basemodel.to_dict())
        self.assertIn("updated_at", basemodel.to_dict())
        self.assertIn("__class__", basemodel.to_dict())

    def test_to_dict_added_attributes(self):
        basemodel = BaseModel()
        basemodel.name = "HOLBERTONACADEMY"
        basemodel.my_number = 98
        self.assertIn("name", basemodel.to_dict())
        self.assertIn("my_number", basemodel.to_dict())

    def test_to_dict_datetime_attributes_are_strings(self):
        basemodel = BaseModel()
        basemodel_dict = basemodel.to_dict()
        self.assertEqual(str, type(basemodel_dict["created_at"]))
        self.assertEqual(str, type(basemodel_dict["updated_at"]))

    def test_to_dict_output(self):
        date_t = datetime.today()
        basemodel = BaseModel()
        basemodel.id = "123456"
        basemodel.created_at = basemodel.updated_at = date_t
        test_dict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': date_t.isoformat(),
            'updated_at': date_t.isoformat()
        }
        self.assertDictEqual(basemodel.to_dict(), test_dict)

    def test_contrast_to_dict_dunder_dict(self):
        basemodel = BaseModel()
        self.assertNotEqual(basemodel.to_dict(), basemodel.__dict__)

    def test_to_dict_with_arg(self):
        basemodel = BaseModel()
        with self.assertRaises(TypeError):
            basemodel.to_dict(None)


if __name__ == "__main__":
    unittest.main()
