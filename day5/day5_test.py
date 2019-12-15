import unittest

from day5 import *


class MyTestCase(unittest.TestCase):

    def testcases(self):
        self.assertEqual([2, 0, 0, 0, 99], run(0, [1, 0, 0, 0, 99]))
        self.assertEqual([2, 3, 0, 6, 99], run(0, [2, 3, 0, 3, 99]))
        self.assertEqual([2, 4, 4, 5, 99, 9801], run(0, [2, 4, 4, 5, 99, 0]))
        self.assertEqual([30, 1, 1, 4, 2, 5, 6, 0, 99], run(0, [1, 1, 1, 4, 99, 5, 6, 0, 99]))

        self.assertEqual([1002, 4, 3, 4, 99], run(0, [1002, 4, 3, 4, 33]))
        self.assertEqual([1101, 100, -1, 4, 99], run(0, [1101, 100, -1, 4, 0]))
