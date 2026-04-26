"""Lecture 1, Interlude 1, Exercise 2 - vector subtraction identities."""

from __future__ import annotations

import pytest

from theoretical_minimum.book1.lecture_01.interlude_01 import exercise_02


def test_componentwise_subtraction_2d_example() -> None:
    assert exercise_02.vector_subtract((3, -1), (2, 4)) == (1.0, -5.0)


def test_subtraction_equals_addition_with_negative() -> None:
    a = (1, 4, -2)
    b = (3, -1, 5)
    left = exercise_02.vector_subtract(a, b)
    right = exercise_02.vector_add(a, exercise_02.vector_negate(b))
    assert left == right


def test_subtract_self_is_zero_vector() -> None:
    v = (2, -7, 0, 3)
    assert exercise_02.vector_subtract(v, v) == (0.0, 0.0, 0.0, 0.0)


def test_mismatched_dimensions_rejected() -> None:
    with pytest.raises(ValueError, match="same dimension"):
        exercise_02.vector_subtract((1, 2), (1, 2, 3))
