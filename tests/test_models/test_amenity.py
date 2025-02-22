#!/usr/bin/python3
""" test description for function """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import unittest
import os


@unittest.skipIf((os.getenv("HBNB_TYPE_STORAGE") == "db"),
                 "Reason usage of DBStorage")
class test_Amenity(test_basemodel):
    """ test description for function """

    def __init__(self, *args, **kwargs):
        """ test description for function """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ test description for function """
        new = self.value()
        self.assertEqual(type(new.name), str)

if __name__ == "__main__":
    unittest.main()
