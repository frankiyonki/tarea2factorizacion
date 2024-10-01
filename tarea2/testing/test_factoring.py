import unittest
from src.calculator import MathCalculator

class TestMathCalculator(unittest.TestCase):
    """
    Unit tests for the MathCalculator class.
    """

    def setUp(self):
        """
        Initializes a new instance of MathCalculator before each test.
        """
        self.calculator = MathCalculator()

    def test_factorial_of_positive_number(self):
        """
        Tests if the factorial of a positive number is calculated correctly.
        """
        self.assertEqual(self.calculator.factorial(3), 6)

    def test_factorial_of_zero(self):
        """
        Tests if the factorial of zero returns 1, as per mathematical definition.
        """
        self.assertEqual(self.calculator.factorial(0), 1)

    def test_factorial_of_negative_number(self):
        """
        Tests if the factorial function raises a ValueError for negative numbers.
        """
        with self.assertRaises(ValueError):
            self.calculator.factorial(-1)



