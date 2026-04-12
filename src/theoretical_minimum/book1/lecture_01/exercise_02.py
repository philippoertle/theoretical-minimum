"""Exercise 2 — Classifying dynamical laws on a six-state system.

Markdown copy (linked from the repo README): ``docs/book1/lecture-01/exercise-02.md``.

A *law* here is deterministic: each face of the die has exactly one successor
state. The lecture examples all preserve information in the sense that each
state also has exactly one *predecessor*; the update is a *permutation* of the
six labels. Such laws are classified, up to relabeling the faces, by the
**cycle type**: the multiset of cycle lengths in the permutation’s disjoint
cycle decomposition (equivalently, a **partition of 6** written with parts in
descending order).

The helpers below encode the four sample laws and compute that partition.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Final

DICE_STATES: Final[frozenset[int]] = frozenset(range(1, 7))

# Dynamical laws from the exercise statement (successor of each state).
EXAMPLE_1: Final[dict[int, int]] = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 1}
EXAMPLE_2: Final[dict[int, int]] = {1: 3, 3: 2, 2: 6, 6: 4, 4: 5, 5: 1}
EXAMPLE_3: Final[dict[int, int]] = {1: 2, 2: 6, 6: 1, 3: 4, 4: 5, 5: 3}
EXAMPLE_4: Final[dict[int, int]] = {1: 1, 2: 3, 3: 4, 4: 2, 5: 6, 6: 5}

EXAMPLES: Final[dict[str, dict[int, int]]] = {
    "example_1": dict(EXAMPLE_1),
    "example_2": dict(EXAMPLE_2),
    "example_3": dict(EXAMPLE_3),
    "example_4": dict(EXAMPLE_4),
}


def cycle_type_descending(successor: Mapping[int, int]) -> tuple[int, ...]:
    """Return cycle lengths of a permutation, sorted descending.

    ``successor`` must be a bijection on its finite domain (each state appears
    exactly once as a key and exactly once as a value).

    Raises:
        ValueError: if the map is not a permutation of its domain.
    """
    domain = set(successor.keys())
    if len(successor) != len(domain):
        msg = "successor map has duplicate keys"
        raise ValueError(msg)
    codomain = set(successor.values())
    if domain != codomain:
        msg = "successor map is not a bijection on its states"
        raise ValueError(msg)

    seen: set[int] = set()
    lengths: list[int] = []
    for start in domain:
        if start in seen:
            continue
        cur = start
        length = 0
        while cur not in seen:
            seen.add(cur)
            cur = successor[cur]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def assert_full_dice_law(successor: Mapping[int, int]) -> None:
    """Check that ``successor`` is a permutation of ``{1, …, 6}``."""
    if set(successor.keys()) != DICE_STATES:
        msg = "keys must be exactly the six die states 1..6"
        raise ValueError(msg)
    if set(successor.values()) != DICE_STATES:
        msg = "values must be exactly the six die states 1..6"
        raise ValueError(msg)
