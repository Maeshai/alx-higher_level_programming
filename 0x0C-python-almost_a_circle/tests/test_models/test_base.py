#!/usr/bin/python3
""" unit test for bases """
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class BaseTestCase(unittest.TestCase):
    """ class for base test """
    def setUp(self):
        """
        Resets id
        """
        Base._Base__nb_objects = 0

    def test_base_task1(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)


if __name__ == '__main__':
    unittest.main()
