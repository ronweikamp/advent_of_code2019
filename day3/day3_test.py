import unittest
from day3 import *


class MyTestCase(unittest.TestCase):

    path1 = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
    path2 = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']

    path11 = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51']
    path22 = ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']

    def testcase1(self):
        self.assertEqual(159, get_manhattan(self.path1, self.path2))

    def testcase2(self):
        self.assertEqual(135, get_manhattan(self.path11, self.path22))

    def test_part2(self):
        self.assertEqual(610, get_min_distance(self.path1, self.path2))
        self.assertEqual(410, get_min_distance(self.path11, self.path22))

if __name__ == '__main__':
    unittest.main()
