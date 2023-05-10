import unittest
from D01 import Day01

class TestD01(unittest.TestCase):

    def test_D01(self):
        self.assertEqual(Day01([(0,1),(1,2)]), 2)
        self.assertEqual(Day01([(0,1),(1,0)]), 1)

if __name__ == '__main__':
    unittest.main()