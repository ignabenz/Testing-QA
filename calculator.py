# calculator_with_tests.py

import unittest

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Tidak dapat membagi dengan nol")
    return x / y

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(subtract(8, 3), 5)

    def test_multiply(self):
        self.assertEqual(multiply(4, 7), 28)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ValueError):
            divide(8, 0)

if __name__ == '__main__':
    unittest.main()