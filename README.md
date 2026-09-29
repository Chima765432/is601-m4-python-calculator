# Professional Calculator

A command-line calculator built in Python. It runs as a REPL, so it keeps
asking for input until you exit. It does addition, subtraction,
multiplication, and division, keeps a history of the session, and has 100
percent test coverage checked by GitHub Actions.

## Structure

- `app/operation` holds the four arithmetic functions.
- `app/calculation` holds the Calculation classes and the factory that builds them.
- `app/calculator` holds the REPL, the history, and the commands.
- `tests` holds the tests for each of those parts.

## Setup

Clone the repo, then from inside the folder:

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Run it

    python main.py

Type an operation as a word, not a symbol: add, subtract, multiply, or
divide. It then asks for two numbers and prints the result.

You can also type:

- `help` to see the operations and commands.
- `history` to see the calculations done this session.
- `exit` to quit.

## Run the tests

    pytest

This runs every test and checks for 100 percent coverage. If coverage drops
below 100, the run fails.
