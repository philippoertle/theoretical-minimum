"""Lecture 2, Exercise 2 — second derivatives vs numeric checks."""

from __future__ import annotations

import math

import pytest

from theoretical_minimum.book1.lecture_02 import exercise_02


def _second_central(fn, z: float, h: float = 2e-5) -> float:
    return (fn(z + h) - 2 * fn(z) + fn(z - h)) / (h * h)


def _f(t: float) -> float:
    return t**4 + 3 * t**3 - 12 * t**2 + t - 6


def _g(x: float) -> float:
    return math.sin(x) - math.cos(x)


def _theta(alpha: float) -> float:
    return math.exp(alpha) + alpha * math.log(alpha)


def _x(t: float) -> float:
    return math.sin(t) ** 2 - math.cos(t)


def test_d2f_dt2_matches_numeric() -> None:
    for t in (-1.4, 0.0, 0.55, 1.8):
        num = _second_central(_f, t)
        assert exercise_02.d2f_dt2(t) == pytest.approx(num, rel=1e-4, abs=1e-4)


def test_d2g_dx2_matches_numeric() -> None:
    for x in (-1.0, 0.0, 0.9, 2.2):
        num = _second_central(_g, x)
        assert exercise_02.d2g_dx2(x) == pytest.approx(num, rel=1e-4, abs=1e-4)


def test_d2theta_dalpha2_matches_numeric() -> None:
    for alpha in (0.25, 0.8, 1.0, 2.0):
        num = _second_central(_theta, alpha)
        assert exercise_02.d2theta_dalpha2(alpha) == pytest.approx(num, rel=1e-4, abs=1e-4)


def test_d2theta_dalpha2_rejects_non_positive() -> None:
    with pytest.raises(ValueError, match="alpha must be > 0"):
        exercise_02.d2theta_dalpha2(0.0)


def test_d2x_dt2_matches_numeric() -> None:
    for t in (-1.0, 0.0, 0.6, 1.7):
        num = _second_central(_x, t)
        assert exercise_02.d2x_dt2(t) == pytest.approx(num, rel=1e-4, abs=1e-4)


def test_book_examples_at_simple_points() -> None:
    assert exercise_02.d2f_dt2(0.0) == -24.0
    assert exercise_02.d2g_dx2(0.0) == 1.0
    assert exercise_02.d2theta_dalpha2(1.0) == pytest.approx(math.e + 1.0)
    assert exercise_02.d2x_dt2(0.0) == 3.0
