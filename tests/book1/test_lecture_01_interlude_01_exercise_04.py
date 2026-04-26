"""Lecture 1, Interlude 1, Exercise 4 - magnitudes, dot product, angle."""

from __future__ import annotations

import math

import pytest

from theoretical_minimum.book1.lecture_01.interlude_01 import exercise_04


def test_exercise_values_match_expected() -> None:
    vals = exercise_04.exercise_values()
    assert vals["magnitude_a"] == pytest.approx(math.sqrt(14.0))
    assert vals["magnitude_b"] == pytest.approx(math.sqrt(29.0))
    assert vals["dot_ab"] == pytest.approx(3.0)
    assert vals["angle_rad"] == pytest.approx(math.acos(3.0 / math.sqrt(406.0)))
    assert vals["angle_deg"] == pytest.approx(81.43753892678774)


def test_angle_rejects_zero_vector() -> None:
    with pytest.raises(ValueError, match="zero vector"):
        exercise_04.angle_between_degrees((0.0, 0.0, 0.0), (1.0, 0.0, 0.0))
