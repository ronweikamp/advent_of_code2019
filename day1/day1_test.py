import unittest
from day1 import *


class TestStringMethods(unittest.TestCase):

    def test_cases_in_exercise(self):
        self.assertEqual(mass_to_fuel(12), 2)
        self.assertEqual(mass_to_fuel(1969), 654)
        self.assertEqual(mass_to_fuel(100756), 33583)

    def test_cases_in_part_2(self):
        self.assertEqual(fuel_to_fuel(2), 0)
        self.assertEqual(fuel_to_fuel(1969), 966)
        self.assertEqual(mass_to_fuel(100756) + fuel_to_fuel(mass_to_fuel(100756)), 50346)


if __name__ == '__main__':
    unittest.main()
    