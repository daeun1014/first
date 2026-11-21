import unittest

from calc import add, calculate, divide, multiply, subtract


class TestBasicOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(divide(10, 4), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


class TestCalculate(unittest.TestCase):
    def test_whole_number_result_has_no_decimal(self):
        self.assertEqual(calculate("10 + 5"), 15)
        self.assertIsInstance(calculate("10 + 5"), int)

    def test_decimal_result(self):
        self.assertEqual(calculate("7 / 2"), 3.5)

    def test_negative_and_decimal_input(self):
        self.assertEqual(calculate("-1.5 * 2"), -3)

    def test_wrong_format(self):
        with self.assertRaises(ValueError):
            calculate("10+5")

    def test_unknown_operator(self):
        with self.assertRaises(ValueError):
            calculate("10 % 3")

    def test_not_a_number(self):
        with self.assertRaises(ValueError):
            calculate("abc + 1")

    def test_infinite_or_nan_input(self):
        for expression in ("inf * 0", "nan + 1", "1e400 + 1"):
            with self.subTest(expression=expression):
                with self.assertRaises(ValueError):
                    calculate(expression)

    def test_result_too_large(self):
        with self.assertRaises(ValueError):
            calculate("1e308 * 10")


if __name__ == "__main__":
    unittest.main()
