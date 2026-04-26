"""Lecture 1, Interlude 1, Exercise 3 - ||A||^2 equals A·A."""

from __future__ import annotations

import pytest

from theoretical_minimum.book1.lecture_01.interlude_01 import exercise_03


def test_example_vector_identity() -> None:
    a = (3, -4, 12)
    assert exercise_03.dot(a, a) == 169.0
    assert exercise_03.magnitude(a) == pytest.approx(13.0)
    assert exercise_03.magnitude(a) ** 2 == pytest.approx(169.0)
    assert exercise_03.magnitude_squared_equals_self_dot(a)


@pytest.mark.parametrize(
    "a",
    [
        (0, 0),
        (1, 2, 3),
        (-2.5, 4.0, 1.5, -7.0),
    ],
)
def test_identity_for_various_vectors(a: tuple[float, ...]) -> None:
    assert exercise_03.magnitude_squared_equals_self_dot(a)


def test_dot_rejects_mismatched_dimensions() -> None:
    with pytest.raises(ValueError, match="same dimension"):
        exercise_03.dot((1, 2), (1, 2, 3))
