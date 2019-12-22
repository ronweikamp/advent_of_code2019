import unittest
from day10 import *

class MyTestCase(unittest.TestCase):

    def testcases(self):
        self.assertEqual(set(), coords_inbetween((0, 0), (1, 1)))
        self.assertEqual({(1, 1)}, coords_inbetween((0, 0), (2, 2)))
        self.assertEqual({(2, 2)}, coords_inbetween((3, 4), (1, 0)))