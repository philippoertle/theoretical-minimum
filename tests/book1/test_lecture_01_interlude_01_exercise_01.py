"""Lecture 1, Interlude 1, Exercise 1 - function definitions and domain checks."""

from __future__ import annotations

import math

import pytest

from theoretical_minimum.book1.lecture_01.interlude_01 import exercise_01


def test_f_of_t_at_zero() -> None:
    assert exercise_01.f_of_t(0.0) == -6.0


def test_g_of_x_at_zero() -> None:
    assert exercise_01.g_of_x(0.0) == -1.0


def test_theta_of_alpha_at_one() -> None:
    # exp(1) + 1*log(1) = e
    assert exercise_01.theta_of_alpha(1.0) == pytest.approx(math.e)


def test_theta_of_alpha_rejects_non_positive() -> None:
    with pytest.raises(ValueError, match="alpha must be > 0"):
        exercise_01.theta_of_alpha(0.0)


@pytest.mark.parametrize(
    ("t", "expected"),
    [
        (0.0, -1.0),
        (math.pi, 1.0),
        (math.pi / 2.0, 1.0),
    ],
)
def test_x_of_t_values(t: float, expected: float) -> None:
    assert exercise_01.x_of_t(t) == pytest.approx(expected)
