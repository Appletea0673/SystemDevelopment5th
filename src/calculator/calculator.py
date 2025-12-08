"""
A simple calculator module with basic arithmetic operations.
"""

MAX_VALUE = 1000000
MIN_VALUE = -1000000


class InvalidInputException(Exception):
    """Exception raised when input values are outside the valid range."""
    pass


class Calculator:
    """Calculator class providing basic arithmetic operations."""

    def _validate_input(self, a, b=None):
        """Validate that input values are within the acceptable range.

        Args:
            a: First number to validate
            b: Second number to validate (optional)

        Raises:
            InvalidInputException: If any input is outside the valid range
        """
        if a < MIN_VALUE or a > MAX_VALUE:
            raise InvalidInputException(f"Input value {a} is outside the valid range [{MIN_VALUE}, {MAX_VALUE}]")
        if b is not None and (b < MIN_VALUE or b > MAX_VALUE):
            raise InvalidInputException(f"Input value {b} is outside the valid range [{MIN_VALUE}, {MAX_VALUE}]")

    def add(self, a, b):
        """Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._validate_input(a, b)
        return a + b

    def subtract(self, a, b):
        """Subtract b from a.

        Args:
            a: First number
            b: Second number

        Returns:
            Difference of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._validate_input(a, b)
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Product of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._validate_input(a, b)
        return a * b

    def divide(self, a, b):
        """Divide a by b.

        Args:
            a: Numerator
            b: Denominator

        Returns:
            Quotient of a and b

        Raises:
            InvalidInputException: If any input is outside valid range or if b is zero
        """
        self._validate_input(a, b)
        if b == 0:
            raise InvalidInputException("Cannot divide by zero")
        return a / b





