#!/usr/bin/python3
""" Module for test Base class """

import unittest
import sys

sys.path.append('../../models')
import base_model
class TestBaseModel(unittest.TestCase):
    """ Suite to test Base class """

    def test_save(self):
        x = base_model.BaseModel()
        before = x.created_at
        x.save()
        after = x.updated_at
        self.assertNotEqual(before, after)

    def test_to_dict(self):
        x = base_model.BaseModel()
        x.to_dict()
        self.assertIsInstance(x.__dict__["my_number"], str)
        self.assertEqual(x.__dict__["__class__"], "BaseModel")
        self.assertEqual(type(x.__dict__), dict)

# if __name__ == "__main__":
    # unittest.main()
