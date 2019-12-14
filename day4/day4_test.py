import unittest
from day4 import *


class MyTestCase(unittest.TestCase):

    def testcases(self):
        self.assertEqual(True, meets_criteria1(111111))
        self.assertEqual(False, meets_criteria1(223450))
        self.assertEqual(False, meets_criteria1(123789))

        self.assertEqual(True, meets_criteria2(112233))
        self.assertEqual(False, meets_criteria2(123444))
        self.assertEqual(True, meets_criteria2(111122))

        
if __name__ == '__main__':
    unittest.main()
