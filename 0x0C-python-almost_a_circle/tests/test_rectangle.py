#!/usr/bin/python3
"""
Unit test for rectangle module.
"""

import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_creat_objects(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)
 
        r2 = Rectangle(10, 2, 1, 1)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 1)
        self.assertEqual(r2.id, 2)
        
        r3 = Rectangle(10, 2, 1, 1, 101)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 1)
        self.assertEqual(r3.y, 1)
        self.assertEqual(r3.id, 101)

    def test_omit_variables(self):
        self.assertRaises(TypeError, Rectangle)
