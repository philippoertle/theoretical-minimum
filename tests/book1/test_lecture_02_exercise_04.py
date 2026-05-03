"""Lecture 2, Exercise 4 — conceptual proofs live in module docstring."""

import theoretical_minimum.book1.lecture_02.exercise_04 as exercise_04


def test_exercise_04_module_docstring_present() -> None:
    doc = exercise_04.__doc__
    assert doc is not None
    assert "Sum rule" in doc
    assert "Product rule" in doc
    assert "Chain rule" in doc
