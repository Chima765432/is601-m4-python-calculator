"""Tests for the calculation classes and the factory."""

import pytest

from app.calculation import (
    CalculationFactory,
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
)


@pytest.mark.parametrize("operation, a, b, expected", [
    ("add", 2, 3, 5),
    ("subtract", 5, 2, 3),
    ("multiply", 4, 3, 12),
    ("divide", 10, 2, 5),
])
def test_factory_creates_and_executes(operation, a, b, expected):
    calculation = CalculationFactory.create(operation, a, b)
    assert calculation.execute() == expected


@pytest.mark.parametrize("operation, expected_class", [
    ("add", AddCalculation),
    ("subtract", SubtractCalculation),
    ("multiply", MultiplyCalculation),
    ("divide", DivideCalculation),
])
def test_factory_returns_right_class(operation, expected_class):
    calculation = CalculationFactory.create(operation, 1, 1)
    assert isinstance(calculation, expected_class)


def test_factory_unknown_operation():
    with pytest.raises(ValueError):
        CalculationFactory.create("power", 2, 3)


def test_divide_calculation_by_zero():
    calculation = CalculationFactory.create("divide", 5, 0)
    with pytest.raises(ZeroDivisionError):
        calculation.execute()
