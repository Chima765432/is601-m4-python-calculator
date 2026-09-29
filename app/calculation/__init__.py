"""Calculation classes and the factory that builds them."""

from app.operation import add, subtract, multiply, divide


class Calculation:
    """Base class for a calculation on two numbers."""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        """Run the calculation and return the result. Overridden by subclasses."""
        raise NotImplementedError  # pragma: no cover


class AddCalculation(Calculation):
    """Addition of two numbers."""

    def execute(self):
        return add(self.a, self.b)


class SubtractCalculation(Calculation):
    """Subtraction of two numbers."""

    def execute(self):
        return subtract(self.a, self.b)


class MultiplyCalculation(Calculation):
    """Multiplication of two numbers."""

    def execute(self):
        return multiply(self.a, self.b)


class DivideCalculation(Calculation):
    """Division of two numbers."""

    def execute(self):
        return divide(self.a, self.b)


class CalculationFactory:
    """Builds the correct Calculation object from an operation name."""

    _calculations = {
        "add": AddCalculation,
        "subtract": SubtractCalculation,
        "multiply": MultiplyCalculation,
        "divide": DivideCalculation,
    }

    @classmethod
    def create(cls, operation, a, b):
        """Return a Calculation for the operation name.

        Uses EAFP: it tries the lookup and catches KeyError for an
        unknown operation.
        """
        try:
            calculation_class = cls._calculations[operation]
        except KeyError:
            raise ValueError(f"Unknown operation: {operation}")
        return calculation_class(a, b)
