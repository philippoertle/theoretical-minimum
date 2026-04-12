"""Lecture 1, Exercise 2 — cycle types of permutation laws on six states."""

import pytest

from theoretical_minimum.book1.lecture_01 import exercise_02


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("example_1", (6,)),
        ("example_2", (6,)),
        ("example_3", (3, 3)),
        ("example_4", (3, 2, 1)),
    ],
)
def test_book_examples_cycle_type(name: str, expected: tuple[int, ...]) -> None:
    law = exercise_02.EXAMPLES[name]
    exercise_02.assert_full_dice_law(law)
    assert exercise_02.cycle_type_descending(law) == expected


def test_non_bijection_rejected() -> None:
    # Two states map to 2, nothing maps to 6 — not a permutation.
    bad = {1: 2, 2: 3, 3: 4, 4: 5, 5: 2, 6: 1}
    with pytest.raises(ValueError, match="bijection"):
        exercise_02.cycle_type_descending(bad)
