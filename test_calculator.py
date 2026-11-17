# https://github.com/Lvl101Magikarp/lab11-AN-KW.git
# Partner 1: Angelina Nguyen
# Partner 2: Kangjian Wong
import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)
        self.assertEqual(calculator.subtract(3, 5), -2)

    def test_multiply(self):
        self.assertEqual(calculator.mul(2, 3), 6)
        self.assertEqual(calculator.mul(-2, 3), -6)
        self.assertEqual(calculator.mul(0, 3), 0)

    def test_divide(self):
        self.assertEqual(calculator.div(6, 3), 2)
        self.assertEqual(calculator.div(-6, 3), -2)
        self.assertEqual(calculator.div(0, 3), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(5, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 8)
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 8)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 5)

    def test_hypotenuse(self):
        self.assertEqual(calculator.hypotenuse(3, 4), 5)
        self.assertEqual(calculator.hypotenuse(5, 12), 13)
        self.assertAlmostEqual(calculator.hypotenuse(1, 1), 1.41421356)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            calculator.square_root(-4)
        self.assertEqual(calculator.square_root(9), 3)
        self.assertEqual(calculator.square_root(0), 0)

if __name__ == "__main__":
    unittest.main()