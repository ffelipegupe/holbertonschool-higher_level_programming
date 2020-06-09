#!/usr/bin/python3
import unittest
import pep8
import json
import sys
import io
from models import base
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestPep8Base(unittest.TestCase):
    """ PEP8 test class for Base
    """
    def pep8_test(self):
        """ Function that checks for PEP8
        """
        guide = pep8.StyleGuide(quite=True)
        file = 'models/base.py'
        file1 = 'tests/test_models/test_base.py'
        res = guide.check_files([file, file1])
        self.assertEqual(res.total_errors, 0, "Erros/Warnings.")

class BaseTest(unittest.TestCase):
    """ Test clase for Base
    """
    @classmethod
    def setUpClass(cls):
        """ Instances for the tests
        """
        Base._Base__nd_objects = 0
        cls.b0 = Base()
        cls.b1 = Base(89)
        cls.b2 = Base()
        cls.b3 = Base()
        cls.b4 = Base(5.5)
        cls.b5 = Base()
        cls.re = Rectangle(2, 1, 0, 0, 2)

    def id_test(self):
        """ id test """
        self.assertEqual(self.b0.id, 1)
        self.assertEqual(self.b1.id, 89)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 5.5)
        self.assertEqual(self.b5.id, 4)
    
    def to_json_test(self):
        """ to_json method test """
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')
        dirct = {"width": 3, "height": 4, "x": 5, "y": 6, "id" = 7}
        json_testing = Base.to_json_string(dirct)
        self.assertTrue(type(json_testing) is str)
        dirct_testing = json.loads(json_testing)
        self.assertSetEqual(dirct_testing, dirct)

    def from_json_test(self):
        """ from_json method test """
        self.assertEqual(Base.from_json_string(None), '[]')
        self.assertEqual(Base.from_json_string([]), '[]')

    @classmethod
    def unsetting(cls):
        """ Instances unsetting """
        pass
