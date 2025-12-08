"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException, MAX_VALUE, MIN_VALUE

class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        calc = Calculator()
        result = calc.add(5, 3)
        assert result == 8
        assert isinstance(result, (int, float))

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        calc = Calculator()
        result = calc.add(-5, -3)
        assert result == -8
        assert result < 0

    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        calc = Calculator()
        result = calc.add(5, -3)
        assert result == 2
        assert result > 0

    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        calc = Calculator()
        result = calc.add(-5, 3)
        assert result == -2
        assert result < 0

    def test_add_positive_with_zero(self):
        """Test adding positive number with zero."""
        calc = Calculator()
        result = calc.add(5, 0)
        assert result == 5
        assert result == 5

    def test_add_zero_with_positive(self):
        """Test adding zero with positive number."""
        calc = Calculator()
        result = calc.add(0, 5)
        assert result == 5
        assert result == 5

    def test_add_floats(self):
        """Test adding floating point numbers."""
        calc = Calculator()
        result = calc.add(2.5, 3.7)
        assert result == pytest.approx(6.2)

    def test_add_large_numbers(self):
        """Test adding large numbers within range."""
        calc = Calculator()
        result = calc.add(999999, 1)
        assert result == 1000000

    def test_add_boundary_max_value(self):
        """Test adding at MAX_VALUE boundary."""
        calc = Calculator()
        result = calc.add(MAX_VALUE, 0)
        assert result == MAX_VALUE

    def test_add_negative_boundary(self):
        """Test adding at MIN_VALUE boundary."""
        calc = Calculator()
        result = calc.add(MIN_VALUE, 0)
        assert result == MIN_VALUE

    def test_add_invalid_positive_a(self):
        """Test adding with first parameter exceeding MAX_VALUE."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(MAX_VALUE + 1, 0)

    def test_add_invalid_positive_b(self):
        """Test adding with second parameter exceeding MAX_VALUE."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(0, MAX_VALUE + 1)

    def test_add_invalid_negative_a(self):
        """Test adding with first parameter below MIN_VALUE."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(MIN_VALUE - 1, 0)

    def test_add_invalid_negative_b(self):
        """Test adding with second parameter below MIN_VALUE."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(0, MIN_VALUE - 1)

    def test_add_commutative(self):
        """Test that addition is commutative (a + b == b + a)."""
        calc = Calculator()
        assert calc.add(7, 3) == calc.add(3, 7)

    def test_add_associative(self):
        """Test that addition is associative ((a + b) + c == a + (b + c))."""
        calc = Calculator()
        assert calc.add(calc.add(2, 3), 4) == calc.add(2, calc.add(3, 4))

class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        calc = Calculator()
        result = calc.subtract(5, 3)
        assert result == 2
        assert isinstance(result, (int, float))

    def test_subtract_negative_numbers(self):
        """Test subtracting two negative numbers."""
        calc = Calculator()
        result = calc.subtract(-5, -3)
        assert result == -2

    def test_subtract_positive_and_negative(self):
        """Test subtracting positive and negative numbers."""
        calc = Calculator()
        result = calc.subtract(5, -3)
        assert result == 8
        assert result > 0

    def test_subtract_negative_and_positive(self):
        """Test subtracting negative and positive numbers."""
        calc = Calculator()
        result = calc.subtract(-5, 3)
        assert result == -8
        assert result < 0

    def test_subtract_positive_with_zero(self):
        """Test subtracting zero from positive number."""
        calc = Calculator()
        result = calc.subtract(5, 0)
        assert result == 5

    def test_subtract_zero_with_positive(self):
        """Test subtracting positive number from zero."""
        calc = Calculator()
        result = calc.subtract(0, 5)
        assert result == -5

    def test_subtract_floats(self):
        """Test subtracting floating point numbers."""
        calc = Calculator()
        result = calc.subtract(5.7, 2.5)
        assert result == pytest.approx(3.2)

    def test_subtract_same_numbers(self):
        """Test subtracting same numbers returns zero."""
        calc = Calculator()
        result = calc.subtract(10, 10)
        assert result == 0

    def test_subtract_boundary_max_value(self):
        """Test subtracting at MAX_VALUE boundary."""
        calc = Calculator()
        result = calc.subtract(MAX_VALUE, 0)
        assert result == MAX_VALUE

    def test_subtract_boundary_min_value(self):
        """Test subtracting at MIN_VALUE boundary."""
        calc = Calculator()
        result = calc.subtract(MIN_VALUE, 0)
        assert result == MIN_VALUE

    def test_subtract_invalid_a(self):
        """Test subtracting with invalid first parameter."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.subtract(MAX_VALUE + 1, 0)

    def test_subtract_invalid_b(self):
        """Test subtracting with invalid second parameter."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.subtract(0, MAX_VALUE + 1)

    def test_subtract_inverse_of_add(self):
        """Test that subtract is inverse of add (a - b + b == a)."""
        calc = Calculator()
        a = 10
        b = 3
        result = calc.add(calc.subtract(a, b), b)
        assert result == pytest.approx(a)

class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        calc = Calculator()
        result = calc.multiply(5, 3)
        assert result == 15
        assert isinstance(result, (int, float))

    def test_multiply_negative_numbers(self):
        """Test multiplying two negative numbers."""
        calc = Calculator()
        result = calc.multiply(-5, -3)
        assert result == 15
        assert result > 0

    def test_multiply_positive_and_negative(self):
        """Test multiplying positive and negative numbers."""
        calc = Calculator()
        result = calc.multiply(5, -3)
        assert result == -15
        assert result < 0

    def test_multiply_negative_and_positive(self):
        """Test multiplying negative and positive numbers."""
        calc = Calculator()
        result = calc.multiply(-5, 3)
        assert result == -15
        assert result < 0

    def test_multiply_positive_with_zero(self):
        """Test multiplying positive number with zero."""
        calc = Calculator()
        result = calc.multiply(5, 0)
        assert result == 0

    def test_multiply_zero_with_positive(self):
        """Test multiplying zero with positive number."""
        calc = Calculator()
        result = calc.multiply(0, 5)
        assert result == 0

    def test_multiply_floats(self):
        """Test multiplying floating point numbers."""
        calc = Calculator()
        result = calc.multiply(2.5, 4.0)
        assert result == pytest.approx(10.0)

    def test_multiply_by_one(self):
        """Test multiplying by one returns the same number."""
        calc = Calculator()
        result = calc.multiply(42, 1)
        assert result == 42

    def test_multiply_by_negative_one(self):
        """Test multiplying by negative one returns negated number."""
        calc = Calculator()
        result = calc.multiply(42, -1)
        assert result == -42

    def test_multiply_large_numbers(self):
        """Test multiplying large numbers."""
        calc = Calculator()
        result = calc.multiply(1000, 500)
        assert result == 500000

    def test_multiply_boundary_max_value(self):
        """Test multiplying at MAX_VALUE boundary."""
        calc = Calculator()
        result = calc.multiply(MAX_VALUE, 1)
        assert result == MAX_VALUE

    def test_multiply_invalid_a(self):
        """Test multiplying with invalid first parameter."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.multiply(MAX_VALUE + 1, 1)

    def test_multiply_invalid_b(self):
        """Test multiplying with invalid second parameter."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.multiply(1, MAX_VALUE + 1)

    def test_multiply_commutative(self):
        """Test that multiplication is commutative (a * b == b * a)."""
        calc = Calculator()
        assert calc.multiply(7, 3) == calc.multiply(3, 7)

class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        calc = Calculator()
        result = calc.divide(10, 2)
        assert result == 5
        assert isinstance(result, (int, float))

    def test_divide_negative_numbers(self):
        """Test dividing two negative numbers."""
        calc = Calculator()
        result = calc.divide(-10, -2)
        assert result == 5
        assert result > 0

    def test_divide_positive_and_negative(self):
        """Test dividing positive and negative numbers."""
        calc = Calculator()
        result = calc.divide(10, -2)
        assert result == -5
        assert result < 0

    def test_divide_negative_and_positive(self):
        """Test dividing negative and positive numbers."""
        calc = Calculator()
        result = calc.divide(-10, 2)
        assert result == -5
        assert result < 0

    def test_divide_positive_with_zero(self):
        """Test dividing positive number by zero raises exception."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(5, 0)

    def test_divide_negative_with_zero(self):
        """Test dividing negative number by zero raises exception."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(-5, 0)

    def test_divide_zero_with_positive(self):
        """Test dividing zero by positive number."""
        calc = Calculator()
        result = calc.divide(0, 5)
        assert result == 0

    def test_divide_zero_with_negative(self):
        """Test dividing zero by negative number."""
        calc = Calculator()
        result = calc.divide(0, -5)
        assert result == 0

    def test_divide_floats(self):
        """Test dividing floating point numbers."""
        calc = Calculator()
        result = calc.divide(10.0, 2.5)
        assert result == pytest.approx(4.0)

    def test_divide_by_one(self):
        """Test dividing by one returns the same number."""
        calc = Calculator()
        result = calc.divide(42, 1)
        assert result == 42

    def test_divide_by_negative_one(self):
        """Test dividing by negative one returns negated number."""
        calc = Calculator()
        result = calc.divide(42, -1)
        assert result == -42

    def test_divide_same_number(self):
        """Test dividing number by itself returns 1."""
        calc = Calculator()
        result = calc.divide(42, 42)
        assert result == pytest.approx(1.0)

    def test_divide_fractional_result(self):
        """Test dividing with fractional result."""
        calc = Calculator()
        result = calc.divide(7, 2)
        assert result == pytest.approx(3.5)

    def test_divide_boundary_max_value(self):
        """Test dividing at MAX_VALUE boundary."""
        calc = Calculator()
        result = calc.divide(MAX_VALUE, 1)
        assert result == MAX_VALUE

    def test_divide_invalid_a(self):
        """Test dividing with invalid first parameter."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(MAX_VALUE + 1, 1)

    def test_divide_invalid_b(self):
        """Test dividing with invalid second parameter (non-zero)."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(10, MAX_VALUE + 1)




