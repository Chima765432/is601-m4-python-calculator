"""Command-line calculator with a REPL, history, and special commands."""

from app.calculation import CalculationFactory


class Calculator:
    """Runs an interactive calculator session."""

    OPERATIONS = ("add", "subtract", "multiply", "divide")

    def __init__(self):
        """Start with an empty history."""
        self.history = []

    def run(self):
        """Run the read-eval-print loop until the user exits."""
        print("Calculator. Operations: add, subtract, multiply, divide.")
        print("Type 'help' for commands or 'exit' to quit.")
        while True:
            command = input("Enter operation: ").strip().lower()
            if command == "exit":
                print("Goodbye.")
                break
            if command == "help":
                self._show_help()
                continue
            if command == "history":
                self._show_history()
                continue
            # LBYL: check the operation is valid before asking for numbers.
            if command not in self.OPERATIONS:
                print(f"Invalid operation: '{command}'. Type 'help' for options.")
                continue
            a = self._read_number("Enter the first number: ")
            if a is None:
                continue
            b = self._read_number("Enter the second number: ")
            if b is None:
                continue
            self._calculate(command, a, b)

    def _read_number(self, prompt):
        """Read a number from the user.

        Uses EAFP: it tries to convert the input to a float and catches the
        ValueError if it is not a number. Returns None on bad input.
        """
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a numeric value.")
            return None

    def _calculate(self, operation, a, b):
        """Create the calculation, run it, record it, and show the result."""
        calculation = CalculationFactory.create(operation, a, b)
        try:
            result = calculation.execute()
        except ZeroDivisionError as error:
            print(error)
            return
        self.history.append(f"{operation} {a} {b} = {result}")
        print(f"Result: {result}")

    def _show_help(self):
        """Print the available commands."""
        print("Operations: add, subtract, multiply, divide.")
        print("Commands: help, history, exit.")

    def _show_history(self):
        """Print the calculations done so far this session."""
        if not self.history:
            print("No calculations yet.")
            return
        for entry in self.history:
            print(entry)
