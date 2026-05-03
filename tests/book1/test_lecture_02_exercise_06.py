"""Tests for Lecture 2, Exercise 6 — SHM period formulas."""

from __future__ import annotations

import math

import pytest

from theoretical_minimum.book1.lecture_02 import exercise_06


def test_period_from_angular_frequency_unit_omega() -> None:
    assert exercise_06.period_from_angular_frequency(1.0) == pytest.approx(2 * math.pi)


def test_period_from_angular_frequency_matches_sqrt_form() -> None:
    m, k = 2.0, 8.0
    omega = math.sqrt(k / m)
    assert exercise_06.period_from_angular_frequency(omega) == pytest.approx(
        exercise_06.period_spring_mass(mass_kg=m, spring_constant=k)
    )


@pytest.mark.parametrize(
    ("omega", "msg"),
    [
        (0.0, "positive"),
        (-1.0, "positive"),
    ],
)
def test_period_from_angular_frequency_rejects_nonpositive_omega(omega: float, msg: str) -> None:
    with pytest.raises(ValueError, match=msg):
        exercise_06.period_from_angular_frequency(omega)


def test_period_spring_mass_numeric() -> None:
    # m=1, k=1 => T = 2*pi
    assert exercise_06.period_spring_mass(mass_kg=1.0, spring_constant=1.0) == pytest.approx(
        2 * math.pi
    )


@pytest.mark.parametrize(
    ("kwargs", "msg"),
    [
        ({"mass_kg": 0.0, "spring_constant": 1.0}, "mass"),
        ({"mass_kg": -1.0, "spring_constant": 1.0}, "mass"),
        ({"mass_kg": 1.0, "spring_constant": 0.0}, "spring_constant"),
        ({"mass_kg": 1.0, "spring_constant": -2.0}, "spring_constant"),
    ],
)
def test_period_spring_mass_validation(kwargs: dict[str, float], msg: str) -> None:
    with pytest.raises(ValueError, match=msg):
        exercise_06.period_spring_mass(**kwargs)
