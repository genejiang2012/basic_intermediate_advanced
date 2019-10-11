# !/usr/bin/env python3
# --*--encoding=utf-8--*--

import unittest
from myfunc import *


class TestMathFunction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        "{}".format("Preparation before class")

    @classmethod
    def tearDownClass(cls):
        "{}".format("Tear down after class")

    def setUp(self):
        "{}".format("preparation for current test case")

    def tearDown(self):
        "{}".format("tear down for current test case")

    def test_add(self):
        self.assertEqual(7, add(3, 4))
        self.assertEqual(5, add(2, 2))

    def test_divide(self):
        self.assertEqual(1, divide(0, 2))
        self.assertEqual(0.5, divide(1, 2))


if __name__ == '__main__':
    unittest.main(verbosity=2)