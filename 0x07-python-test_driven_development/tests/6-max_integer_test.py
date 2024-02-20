#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_value(self):
        self.assertEqual(max_integer([1, 5, 10, 8]), 10)
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([-123, -5, -1000, -1, -35]), -1)
        self.assertEqual(max_integer([100, 1, 2]), 100)
        self.assertEqual(max_integer([100, 1, 200]), 200)
        self.assertEqual(max_integer([1]), 1)

    def test_type(self):
        self.assertRaises(TypeError, max_integer, 1)
        self.assertRaises(TypeError, max_integer, ['akram', 1])
