

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(calculator.sub(5, 3), 2)
        self.assertEqual(calculator.sub(3, 5), -2)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.multiply(-2, 3), -6)
        self.assertEqual(calculator.multiply(0, 3), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(calculator.divide(6, 3), 2)
        self.assertEqual(calculator.divide(-6, 3), -2)
        self.assertEqual(calculator.divide(0, 3), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.log(2, 8), 3.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.log(1, 8)
        with self.assertRaises(ValueError):
            calculator.log(-2, 8)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code
        with self.assertRaises(ValueError):
            calculator.log(0, 5)

    def test_hypotenuse(self): # 3 assertions
    #     fill in code
        self.assertEqual(calculator.hypotenuse(3, 4), 5)
        self.assertEqual(calculator.hypotenuse(5, 12), 13)
        self.assertAlmostEqual(calculator.hypotenuse(1, 1), 1.41421356)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################
        with self.assertRaises(ValueError):
            calculator.square_root(-4)
        self.assertEqual(calculator.square_root(9), 3)
        self.assertEqual(calculator.square_root(0), 0)

# Do not touch this
if __name__ == "__main__":
    unittest.main()