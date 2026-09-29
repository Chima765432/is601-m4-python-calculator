"""Tests for the arithmetic operations."""

import pytest

from app.operation import add, subtract, multiply, divide


@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (-1, 1, 0), (0, 0, 0)])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(5, 3, 2), (0, 4, -4), (-2, -2, 0)])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(2, 3, 6), (-2, 3, -6), (0, 5, 0)])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(6, 3, 2), (5, 2, 2.5), (-6, 2, -3)])
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
