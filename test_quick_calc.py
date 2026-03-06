import pytest
from quick_calc import QuickCalc

calc = QuickCalc()

def test_addition():
    assert calc.add(5, 3) == 8

def test_subtraction():
    assert calc.subtract(10, 4) == 6

def test_multiplication():
    assert calc.multiply(6, 7) == 42

def test_division():
    assert calc.divide(8, 2) == 4

def test_division_by_zero():
    assert calc.divide(5, 0) == "Error: Division by zero"

def test_negative_numbers():
    assert calc.add(-2, -3) == -5

def test_decimal_numbers():
    assert calc.multiply(2.5, 4) == 10.0

def test_large_numbers():
    assert calc.add(1e10, 1e10) == 2e10

def test_integration_add_and_clear():
    calc.result = calc.add(5, 3)
    assert calc.result == 8
    calc.reset()
    assert calc.result == 0

def test_integration_sequence():
    result = calc.calculate('+', 5, 3)
    assert result == 8
    result = calc.calculate('*', result, 2)
    assert result == 16
