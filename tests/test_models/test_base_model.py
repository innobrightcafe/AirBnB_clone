#!/usr/bin/python3
""" Module for test Base class """
import unittest
from models.base_model import Base_model
from io import StringIO
from unittest import TestCase
from unittest.mock import patch


class TestBaseMethods(unittest.TestCase):
    """ Suite to test Base class """

    