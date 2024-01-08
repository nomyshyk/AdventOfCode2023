import unittest

import Day3


class MyTestCase(unittest.TestCase):
    def test_something(self):
        x = Day3.test_return()
        self.assertEqual(x, "nice")  # add assertion here


if __name__ == '__main__':
    unittest.main()
