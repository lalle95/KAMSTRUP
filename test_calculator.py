import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(10, 5), 15)
        self.assertEqual(calculator.add(-2, -2), -4)
        self.assertEqual(calculator.add(-2, 2), 0)
        self.assertEqual(calculator.add(2, 2), 4)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.subtract(5, -5), 10)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 5), 2)
        with self.assertRaises(ValueError):
            calculator.divide(10, 0)

    def test_formatter(self):
        self.assertIsInstance(calculator.formatter(5), str)


if __name__ == '__main__':
    unittest.main()
