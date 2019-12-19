import unittest

from day5 import *


class MyTestCase(unittest.TestCase):

    def testcases(self):
        self.assertEqual([2, 0, 0, 0, 99], run(0, [1, 0, 0, 0, 99])[0])
        self.assertEqual([2, 3, 0, 6, 99], run(0, [2, 3, 0, 3, 99])[0])
        self.assertEqual([2, 4, 4, 5, 99, 9801], run(0, [2, 4, 4, 5, 99, 0])[0])
        self.assertEqual([30, 1, 1, 4, 2, 5, 6, 0, 99], run(0, [1, 1, 1, 4, 99, 5, 6, 0, 99])[0])

        self.assertEqual([1002, 4, 3, 4, 99], run(0, [1002, 4, 3, 4, 33])[0])
        self.assertEqual([1101, 100, -1, 4, 99], run(0, [1101, 100, -1, 4, 0])[0])

    def testcases2(self):
        init_state = [3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1, 192, 154, 224, 101, -161, 224, 224, 4, 224,
                      102, 8, 223, 223,
                      101, 5, 224, 224, 1, 223, 224, 223, 1001, 157, 48, 224, 1001, 224, -61, 224, 4, 224, 102, 8, 223,
                      223, 101, 2, 224,
                      224, 1, 223, 224, 223, 1102, 15, 28, 225, 1002, 162, 75, 224, 1001, 224, -600, 224, 4, 224, 1002,
                      223, 8, 223,
                      1001, 224, 1, 224, 1, 224, 223, 223, 102, 32, 57, 224, 1001, 224, -480, 224, 4, 224, 102, 8, 223,
                      223, 101, 1, 224,
                      224, 1, 224, 223, 223, 1101, 6, 23, 225, 1102, 15, 70, 224, 1001, 224, -1050, 224, 4, 224, 1002,
                      223, 8, 223, 101,
                      5, 224, 224, 1, 224, 223, 223, 101, 53, 196, 224, 1001, 224, -63, 224, 4, 224, 102, 8, 223, 223,
                      1001, 224, 3, 224,
                      1, 224, 223, 223, 1101, 64, 94, 225, 1102, 13, 23, 225, 1101, 41, 8, 225, 2, 105, 187, 224, 1001,
                      224, -60, 224, 4,
                      224, 1002, 223, 8, 223, 101, 6, 224, 224, 1, 224, 223, 223, 1101, 10, 23, 225, 1101, 16, 67, 225,
                      1101, 58, 10,
                      225, 1101, 25, 34, 224, 1001, 224, -59, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 3, 224, 1, 223,
                      224, 223, 4,
                      223, 99, 0, 0, 0, 677, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105, 0, 99999, 1105, 227, 247, 1105, 1,
                      99999, 1005, 227,
                      99999, 1005, 0, 256, 1105, 1, 99999, 1106, 227, 99999, 1106, 0, 265, 1105, 1, 99999, 1006, 0,
                      99999, 1006, 227,
                      274, 1105, 1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225, 225, 1101, 294, 0, 0, 105, 1, 0,
                      1105, 1, 99999,
                      1106, 0, 300, 1105, 1, 99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0, 0, 1105, 1, 99999, 1108,
                      226, 226, 224,
                      102, 2, 223, 223, 1005, 224, 329, 101, 1, 223, 223, 107, 226, 226, 224, 1002, 223, 2, 223, 1005,
                      224, 344, 1001,
                      223, 1, 223, 107, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 359, 101, 1, 223, 223, 7, 677, 226,
                      224, 102, 2, 223,
                      223, 1005, 224, 374, 101, 1, 223, 223, 108, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 389, 101,
                      1, 223, 223,
                      1007, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 404, 101, 1, 223, 223, 7, 226, 677, 224, 102, 2,
                      223, 223, 1006,
                      224, 419, 101, 1, 223, 223, 1107, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 434, 1001, 223, 1,
                      223, 1108, 226,
                      677, 224, 102, 2, 223, 223, 1005, 224, 449, 101, 1, 223, 223, 108, 226, 677, 224, 102, 2, 223,
                      223, 1005, 224, 464,
                      1001, 223, 1, 223, 8, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 479, 1001, 223, 1, 223, 1007,
                      226, 226, 224,
                      102, 2, 223, 223, 1006, 224, 494, 101, 1, 223, 223, 1008, 226, 677, 224, 102, 2, 223, 223, 1006,
                      224, 509, 101, 1,
                      223, 223, 1107, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 524, 1001, 223, 1, 223, 108, 677,
                      677, 224, 1002, 223,
                      2, 223, 1005, 224, 539, 1001, 223, 1, 223, 1107, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 554,
                      1001, 223, 1,
                      223, 7, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 569, 1001, 223, 1, 223, 8, 677, 226, 224,
                      102, 2, 223, 223,
                      1006, 224, 584, 101, 1, 223, 223, 1008, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 599, 101, 1,
                      223, 223, 1007,
                      226, 677, 224, 1002, 223, 2, 223, 1006, 224, 614, 1001, 223, 1, 223, 8, 677, 677, 224, 1002, 223,
                      2, 223, 1005,
                      224, 629, 101, 1, 223, 223, 107, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 644, 101, 1, 223,
                      223, 1108, 677, 226,
                      224, 102, 2, 223, 223, 1005, 224, 659, 101, 1, 223, 223, 1008, 226, 226, 224, 102, 2, 223, 223,
                      1006, 224, 674,
                      1001, 223, 1, 223, 4, 223, 99, 226
                      ]

        self.assertEqual(11049715, run(0, init_state, [1])[1])
        self.assertEqual(2140710, run(0, init_state, [5])[1])

