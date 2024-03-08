#!/usr/bin/python3
"""
Unit test for base module.
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_creat_objects(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(101)
        self.assertEqual(b2.id, 101)

        b3 = Base()
        self.assertEqual(b3.id, 2)
