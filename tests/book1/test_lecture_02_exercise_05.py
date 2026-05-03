"""Lecture 2, Exercise 5 — conceptual proofs live in module docstring."""

import theoretical_minimum.book1.lecture_02.exercise_05 as exercise_05


def test_exercise_05_module_docstring_present() -> None:
    doc = exercise_05.__doc__
    assert doc is not None
    assert "sin" in doc
    assert "cos" in doc
    assert "exp" in doc or "e^t" in doc
    assert "ln" in doc
