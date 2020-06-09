#!/usr/bin/python3
import unittest
import pep8
import json
import sys
import io
from models import rectangle
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestPep8Rectangle(unittest.TestCase):
    """ PEP8 test class for Rectangle
    """
    def pep8_test(self):
        """ Function that checks for PEP8
        """
        guide = pep8.StyleGuide(quite=True)
        file = 'models/rectangle.py'
        file1 = 'tests/test_models/test_rectangle.py'
        res = guide.check_files([file, file1])
        self.assertEqual(res.total_errors, 0, "Erros/Warnings.")

class BaseTest(unittest.TestCase):
    """ Test clase for Rectangle
    """
    @classmethod
    def setUpClass(cls):
        """ Instances for the tests
        """
        Base._Base__nd_objects = 0
        cls.r0 = Rectangle(2, 1, 0, 0, 10)
        cls.r1 = Rectangle(10, 10, 2)
        cls.r2 = Rectangle(2, 2, 2)
        cls.r3 = Rectangle(7, 8, 9, 10)

    def id_test(self):
        """ id test """
        self.assertEqual(self.r0.id, 10)
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 3)

