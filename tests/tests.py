import unittest
from unittest import TestCase
from app import calc, divide

class TestCal(TestCase):
    def test_calc(self):
        self.assertEqual(calc(1, 2), 3)

    def test_divide(self):
        self.assertEqual(divide(1, 0), 1)
        with self.assertRaises(TypeError):
            print(TypeError)

if __name__ == '__main__':
    tests = TestCal()
    tests.test_calc()
    tests.test_divide()