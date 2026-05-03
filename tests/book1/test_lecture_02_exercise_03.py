"""Lecture 2, Exercise 3 — chain-rule derivatives vs numeric checks."""

from __future__ import annotations

import math

import pytest

from theoretical_minimum.book1.lecture_02 import exercise_03


def _central_derivative(fn, z: float, h: float = 1e-7) -> float:
    return (fn(z + h) - fn(z - h)) / (2 * h)


def _g(t: float) -> float:
    u = t * t
    return math.sin(u) - math.cos(u)


def _theta(alpha: float) -> float:
    return math.exp(3 * alpha) + 3 * alpha * math.log(3 * alpha)


def _x(t: float) -> float:
    u = t * t
    return math.sin(u) ** 2 - math.cos(u)


def test_dg_dt_matches_numeric() -> None:
    for t in (-1.1, 0.0, 0.55, 1.4):
        num = _central_derivative(_g, t)
        assert exercise_03.dg_dt(t) == pytest.approx(num, rel=1e-5, abs=1e-5)


def test_dtheta_dalpha_matches_numeric() -> None:
    for alpha in (0.15, 0.7, 1.0, 1.6):
        num = _central_derivative(_theta, alpha)
        assert exercise_03.dtheta_dalpha(alpha) == pytest.approx(num, rel=1e-5, abs=1e-5)


def test_dtheta_dalpha_rejects_non_positive() -> None:
    with pytest.raises(ValueError, match="alpha must be > 0"):
        exercise_03.dtheta_dalpha(0.0)


def test_dx_dt_matches_numeric() -> None:
    for t in (-0.9, 0.0, 0.45, 1.2):
        num = _central_derivative(_x, t)
        assert exercise_03.dx_dt(t) == pytest.approx(num, rel=1e-5, abs=1e-5)


def test_spot_values() -> None:
    assert exercise_03.dg_dt(0.0) == 0.0
    assert exercise_03.dx_dt(0.0) == 0.0
    assert exercise_03.dtheta_dalpha(1.0) == pytest.approx(3 * math.exp(3) + 3 * math.log(3) + 3)
