"""Lecture 1, Exercise 1 — conceptual answer is in module docstring."""

import theoretical_minimum.book1.lecture_01.exercise_01 as exercise_01


def test_exercise_01_module_docstring_present() -> None:
    doc = exercise_01.__doc__
    assert doc is not None
    assert "Closed system" in doc
    assert "Open system" in doc
    assert "Implicit assumptions" in doc
