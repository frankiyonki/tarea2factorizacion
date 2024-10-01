import math

class MathCalculator:
    """
    A simple scientific calculator that performs basic arithmetic 
    operations and some advanced mathematical functions like factorial.
    """

    def add(self, a, b):
        """
        Returns the sum of two numbers.
        """
        return a + b

    def subtract(self, a, b):
        """
        Returns the difference between two numbers.
        """
        return a - b

    def multiply(self, a, b):
        """
        Returns the product of two numbers.
        """
        return a * b

    def divide(self, a, b):
        """
        Returns the result of dividing the first number by the second.
        Raises a ValueError if the second number is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def factorial(self, number):
        """
        Returns the factorial of a non-negative integer.
        Raises a ValueError for negative numbers.
        """
        if number < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        elif number == 0:
            return 1
        fact = 1
        for i in range(1, number + 1):
            fact *= i
        return fact
