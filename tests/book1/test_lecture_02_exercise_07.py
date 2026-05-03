"""Tests for Lecture 2, Exercise 7 — orthogonality in uniform circular motion."""

from __future__ import annotations

import math

import pytest

from theoretical_minimum.book1.lecture_02 import exercise_07


@pytest.mark.parametrize("t", [0.0, 0.37, 1.2, -0.55, math.pi / 4])
def test_velocity_acceleration_orthogonal(t: float) -> None:
    dot_va = exercise_07.velocity_acceleration_dot(radius=2.5, omega=1.7, t=t)
    assert dot_va == pytest.approx(0.0, abs=1e-12)


@pytest.mark.parametrize("omega", [-2.0, 0.0, 3.0])
@pytest.mark.parametrize("t", [0.11, 0.9])
def test_velocity_acceleration_orthogonal_various_omega(omega: float, t: float) -> None:
    dot_va = exercise_07.velocity_acceleration_dot(radius=1.0, omega=omega, t=t)
    assert dot_va == pytest.approx(0.0, abs=1e-12)


@pytest.mark.parametrize("t", [0.0, 0.61, -0.2])
def test_position_velocity_orthogonal(t: float) -> None:
    dot_rv = exercise_07.position_velocity_dot(radius=1.25, omega=0.9, t=t)
    assert dot_rv == pytest.approx(0.0, abs=1e-12)


def test_radius_must_be_positive() -> None:
    with pytest.raises(ValueError, match="radius"):
        exercise_07.velocity_ucm(radius=0.0, omega=1.0, t=0.0)
    with pytest.raises(ValueError, match="radius"):
        exercise_07.acceleration_ucm(radius=-1.0, omega=1.0, t=0.0)
    with pytest.raises(ValueError, match="radius"):
        exercise_07.position_ucm(radius=-0.5, omega=1.0, t=0.0)
