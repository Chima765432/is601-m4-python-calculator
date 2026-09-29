"""Tests for the calculator REPL."""

from app.calculator import Calculator


def run_with_inputs(monkeypatch, inputs):
    """Run the calculator feeding it the given inputs in order."""
    queue = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(queue))
    Calculator().run()


def test_exit(monkeypatch, capsys):
    run_with_inputs(monkeypatch, ["exit"])
    assert "Goodbye" in capsys.readouterr().out


def test_help(monkeypatch, capsys):
    run_with_inputs(monkeypatch, ["help", "exit"])
    assert "Commands: help, history, exit." in capsys.readouterr().out


def test_history_empty(monkeypatch, capsys):
    run_with_inputs(monkeypatch, ["history", "exit"])
    assert "No calculations yet." in capsys.readouterr().out


def test_valid_calculation(monkeypatch, capsys):
    run_with_inputs(monkeypatch, ["add", "2", "3", "exit"])
    assert "Result: 5.0" in capsys.readouterr().out


def test_history_after_calculation(monkeypatch, capsys):
    run_with_inputs(monkeypatch, ["add", "2", "3", "history", "exit"])
    assert "add 2.0 3.0 = 5.0" in capsys.readouterr().out


def test_invalid_operation(monkeypatch, capsys):
    run_with_inputs(monkeypatch, ["foo", "exit"])
    assert "Invalid operation" in capsys.readouterr().out


def test_invalid_first_number(monkeypatch, capsys):
    run_with_inputs(monkeypatch, ["add", "abc", "exit"])
    assert "Invalid number" in capsys.readouterr().out


def test_invalid_second_number(monkeypatch, capsys):
    run_with_inputs(monkeypatch, ["add", "2", "abc", "exit"])
    assert "Invalid number" in capsys.readouterr().out


def test_divide_by_zero(monkeypatch, capsys):
    run_with_inputs(monkeypatch, ["divide", "5", "0", "exit"])
    assert "Cannot divide by zero" in capsys.readouterr().out
