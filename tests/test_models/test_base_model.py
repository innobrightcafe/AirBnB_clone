#!/usr/bin/python3
""" Module for test Base class """
import unittest
from models.base_model import Base_model
from models.user import User
from io import StringIO
from unittest import TestCase
from unittest.mock import patch


class TestBaseMethods(unittest.TestCase):
    """ Suite to test Base class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0