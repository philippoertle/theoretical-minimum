"""Lecture 2, Exercise 1 — closed-form derivatives vs numeric checks."""

from __future__ import annotations

import math

import pytest

from theoretical_minimum.book1.lecture_02 import exercise_01


def _central_derivative(fn, z: float, h: float = 1e-7) -> float:
    return (fn(z + h) - fn(z - h)) / (2 * h)


def _f(t: float) -> float:
    return t**4 + 3 * t**3 - 12 * t**2 + t - 6


def _g(x: float) -> float:
    return math.sin(x) - math.cos(x)


def _theta(alpha: float) -> float:
    return math.exp(alpha) + alpha * math.log(alpha)


def _x(t: float) -> float:
    return math.sin(t) ** 2 - math.cos(t)


def test_df_dt_matches_numeric() -> None:
    for t in (-1.7, 0.0, 0.42, 2.1):
        num = _central_derivative(_f, t)
        assert exercise_01.df_dt(t) == pytest.approx(num, rel=1e-5, abs=1e-5)


def test_dg_dx_matches_numeric() -> None:
    for x in (-0.9, 0.0, 1.1, 2.6):
        num = _central_derivative(_g, x)
        assert exercise_01.dg_dx(x) == pytest.approx(num, rel=1e-5, abs=1e-5)


def test_dtheta_dalpha_matches_numeric() -> None:
    for alpha in (0.2, 0.9, 1.0, 2.3):
        num = _central_derivative(_theta, alpha)
        assert exercise_01.dtheta_dalpha(alpha) == pytest.approx(num, rel=1e-5, abs=1e-5)


def test_dtheta_dalpha_rejects_non_positive() -> None:
    with pytest.raises(ValueError, match="alpha must be > 0"):
        exercise_01.dtheta_dalpha(0.0)


def test_dx_dt_matches_numeric() -> None:
    for t in (-1.2, 0.0, 0.7, 1.9):
        num = _central_derivative(_x, t)
        assert exercise_01.dx_dt(t) == pytest.approx(num, rel=1e-5, abs=1e-5)


def test_book_examples_at_simple_points() -> None:
    assert exercise_01.df_dt(0.0) == 1.0
    assert exercise_01.dg_dx(0.0) == 1.0
    assert exercise_01.dtheta_dalpha(1.0) == pytest.approx(math.e + 1.0)
    assert exercise_01.dx_dt(0.0) == 0.0
