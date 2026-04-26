"""Lecture 1, Exercise 3 — allowable laws on ℤ."""

import pytest

from theoretical_minimum.book1.lecture_01 import exercise_03


def test_eq4_collision_breaks_injectivity() -> None:
    a, b = exercise_03.square_law_collides_distinct_integers()
    assert a != b
    assert exercise_03.step_eq4_square(a) == exercise_03.step_eq4_square(b)


def test_two_is_not_an_integer_square() -> None:
    assert exercise_03.integer_square_roots_of_two_exist() is False


@pytest.mark.parametrize("radius", [5, 20])
def test_eq5_bijection_on_interval(radius: int) -> None:
    assert exercise_03.eq5_is_bijection_on_symmetric_interval(radius)


@pytest.mark.parametrize(
    "n",
    [-17, -2, -1, 0, 1, 2, 9],
)
def test_eq5_preimage_is_inverse(n: int) -> None:
    f = exercise_03.step_eq5_sign_flip
    m = f(n)
    assert exercise_03.preimage_eq5(m) == n


def test_eq2_eq3_are_global_bijections_via_inverses() -> None:
    """f(n)=n+1 and f(n)=n+2 are permutations of Z: each has a two-sided inverse."""
    f2 = exercise_03.step_eq2_plus_one
    f3 = exercise_03.step_eq3_plus_two
    for n in range(-400, 401):
        assert f2(n) - 1 == n
        assert f2(n - 1) == n
        assert f3(n) - 2 == n
        assert f3(n - 2) == n


def test_eq4_not_bijection_on_small_interval_containing_collision() -> None:
    assert not exercise_03.is_bijection_on_interval(exercise_03.step_eq4_square, -3, 3)
