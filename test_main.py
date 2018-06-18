import unittest

import main


class TestMathMethods(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(6, main.multiply(2, 3))

    def test_divide(self):
        self.assertEqual(3, main.divide(6, 2))

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            main.divide(6, 0)


if __name__ == '__main__':
    unittest.main()
