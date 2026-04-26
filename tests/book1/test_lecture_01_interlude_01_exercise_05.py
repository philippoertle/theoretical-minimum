"""Lecture 1, Interlude 1, Exercise 5 - orthogonal vector pairs."""

from __future__ import annotations

from theoretical_minimum.book1.lecture_01.interlude_01 import exercise_05


def test_pairwise_dot_products() -> None:
    dots = exercise_05.all_pairwise_dot_products()
    assert dots[("v1", "v2")] == 4.0
    assert dots[("v1", "v3")] == 4.0
    assert dots[("v1", "v4")] == -1.0
    assert dots[("v2", "v3")] == 5.0
    assert dots[("v2", "v4")] == 0.0
    assert dots[("v3", "v4")] == -9.0


def test_orthogonal_pair_detection() -> None:
    assert exercise_05.orthogonal_pairs() == [("v2", "v4")]
