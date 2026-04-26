"""Lecture 1, Interlude 1, Exercise 6 - orthogonality and dot product."""

from __future__ import annotations

import math

import pytest

from theoretical_minimum.book1.lecture_01.interlude_01 import exercise_06


def test_perpendicular_2d_vectors_have_zero_dot() -> None:
    a = (1.0, 0.0)
    b = (0.0, 5.0)
    assert exercise_06.dot(a, b) == pytest.approx(0.0)
    assert exercise_06.is_orthogonal(a, b)
    assert exercise_06.angle_between_radians(a, b) == pytest.approx(math.pi / 2.0)


def test_orthogonal_3d_example_has_zero_dot() -> None:
    a = (2.0, -1.0, 3.0)
    b = (-3.0, 0.0, 2.0)
    assert exercise_06.dot(a, b) == pytest.approx(0.0)
    assert exercise_06.is_orthogonal(a, b)


def test_non_orthogonal_vectors_not_flagged() -> None:
    a = (1.0, 2.0)
    b = (2.0, 1.0)
    assert exercise_06.dot(a, b) == pytest.approx(4.0)
    assert not exercise_06.is_orthogonal(a, b)
