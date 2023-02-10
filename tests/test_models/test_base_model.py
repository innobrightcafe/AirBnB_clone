#!/usr/bin/python3
""" Module for test Base class """

import unittest
import datetime
import models.base_model
class TestBaseModel(unittest.TestCase):
    """ Suite to test Base class """

    def test_id(self):
        self.assertTrue(self.base_model.id, str)
        self.assertNotEqual(self.base_model.id, "")
    def test_created_at(self):
        self.assertTrue(self.base_model.created_at, datetime.datetime)

    def test_updated_at(self):
        self.assertTrue(self.base_model.updated_at, datetime.datetime)

    def test_save(self):
        before = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(before, self.base_model.updated_at)

    def test_to_dict(self):
        result = self.base_model.to_dict()
        self.assertIsInstance(result["updated_at"], str)
        self.assertEqual(result["__class__"], "BaseModel")
        self.assertEqual(type(result), dict)

if __name__ == "__main__":
    unittest.main()
