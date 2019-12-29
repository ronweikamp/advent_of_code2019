import unittest
from day14 import *

class MyTestCase(unittest.TestCase):

    def testcases(self):
        self.assertEqual(31, min_ORE_needed(get_init_state('test_input'), 1))
        self.assertEqual(165, min_ORE_needed(get_init_state('test_input2'), 1))
        self.assertEqual(13312, min_ORE_needed(get_init_state('test_input3'), 1))
        self.assertEqual(180697, min_ORE_needed(get_init_state('test_input4'), 1))
        self.assertEqual(2210736, min_ORE_needed(get_init_state('test_input5'), 1))

