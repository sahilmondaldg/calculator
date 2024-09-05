# test_calculator.py
import unittest
from calculator import add, subtract, multiply

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 2), 5)
        self.assertEqual(add(0, 5), 5)
        with self.assertRaises(ValueError):
            add(-1, 3)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10, 5), 5)
        with self.assertRaises(ValueError):
            subtract(4, -1)

    def test_multiply(self):
        self.assertEqual(multiply(3, 2), 6)
        self.assertEqual(multiply(0, 5), 0)
        with self.assertRaises(ValueError):
            multiply(-2, 3)

if __name__ == "__main__":
    unittest.main()
