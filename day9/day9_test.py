import unittest
from day9 import run_with_mem, get_init_state


class MyTestCase(unittest.TestCase):

    def testcases(self):
        self.assertEqual([109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99], run_with_mem(
            [109, 1, 204,
             -1, 1001, 100,
             1, 100, 1008,
             100, 16, 101,
             1006, 101,
             0, 99]))

        self.assertEqual([1219070632396864], run_with_mem([1102, 34915192, 34915192, 7, 4, 7, 99, 0]))

        self.assertEqual([1125899906842624], run_with_mem([104, 1125899906842624, 99]))

    def testcases_part_1(self):
        self.assertEqual([3345854957], run_with_mem(get_init_state(), inputs=[1]))


    def testcases_part_2(self):
        self.assertEqual([68938], run_with_mem(get_init_state(), inputs=[2]))
