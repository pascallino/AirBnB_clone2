#!/usr/bin/python3
""" unit test for Based Model

unittest class:
        Base Model Class
"""

from time import sleep
import sys
import os
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel_Init(unittest.TestCase):
    """ testing the BaseModel ___init___ method """

    def test_no_arg_init(self):
        """ test for no arguements """
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_BaseModel_id(self):
        """ test for BaseMOdel id """
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_typeof_datetime(self):
        """ test the type for the created_at """
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_typeof_datetime(self):
        """ test the type for the updated_at """
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_instanceid_are_different(self):
        """ test two id's of two instances """
        Base1 = BaseModel()
        Base2 = BaseModel()
        self.assertNotEqual(Base1.id, Base2.id)

    def test_different_instantiation(self):
        """Tests instantiation of BaseModel class."""

        b = BaseModel()
        self.assertEqual(str(type(b)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_different_updated_at(self):
        """ Test for two different dates """
        base1 = BaseModel()
        sleep(0.10)
        base2 = BaseModel()
        self.assertLess(base1.updated_at, base2.updated_at)

    def test_different_created_at(self):
        """ Test for two different dates """
        base1 = BaseModel()
        sleep(0.10)
        base2 = BaseModel()
        self.assertLess(base1.created_at, base2.created_at)

    def test_for_none_arg(self):
        """ test for None values in keys """
        base1 = BaseModel(None)
        self.assertNotIn(None, base1.__dict__.values())

    def test_dict_keys_values(self):
        """Tests for the to_dict(). """

        base1 = BaseModel()
        base1.name = "Pascal"
        base1.age = 28
        bcopy = base1.to_dict()
        self.assertEqual(bcopy["id"], base1.id)
        self.assertEqual(bcopy["__class__"], type(base1).__name__)
        self.assertEqual(bcopy["created_at"], base1.created_at.isoformat())
        self.assertEqual(bcopy["updated_at"], base1.updated_at.isoformat())
        self.assertEqual(bcopy["name"], base1.name)
        self.assertEqual(bcopy["age"], base1.age)


if __name__ == '__main__':
    unittest.main()
