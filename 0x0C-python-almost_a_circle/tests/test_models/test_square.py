#!/usr/bin/python3
import unittest
import pep8
import json
import sys
import io
from models import square
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestPep8Square(unittest.TestCase):
    """ PEP8 test class for Rectangle
    """
    def pep8_test(self):
        """ Function that checks for PEP8
        """
        guide = pep8.StyleGuide(quite=True)
        file = 'models/square.py'
        file1 = 'tests/test_models/test_square.py'
        res = guide.check_files([file, file1])
        self.assertEqual(res.total_errors, 0, "Erros/Warnings.")
