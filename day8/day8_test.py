import unittest
from day8 import get_layers

class MyTestCase(unittest.TestCase):

    def testcases(self):
        self.assertEqual(['123456', '789012'], get_layers(3,2, '123456789012', []))
