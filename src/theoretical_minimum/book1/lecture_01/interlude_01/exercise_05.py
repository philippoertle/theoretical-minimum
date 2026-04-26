"""Interlude 1, Exercise 5 - determine orthogonal vector pairs.

TeX/PDF write-up (linked from the repo README):
``docs/book1/lecture-01/interlude-01/exercise-05.tex``,
``docs/book1/lecture-01/interlude-01/exercise-05.pdf``.
"""

from __future__ import annotations

from collections.abc import Sequence
from itertools import combinations

V1: tuple[int, int, int] = (1, 1, 1)
V2: tuple[int, int, int] = (2, -1, 3)
V3: tuple[int, int, int] = (3, 1, 0)
V4: tuple[int, int, int] = (-3, 0, 2)

VECTORS: dict[str, tuple[int, int, int]] = {
    "v1": V1,
    "v2": V2,
    "v3": V3,
    "v4": V4,
}


def dot(a: Sequence[int | float], b: Sequence[int | float]) -> float:
    """Return Euclidean dot product of vectors ``a`` and ``b``."""
    if len(a) != len(b):
        msg = "vectors must have the same dimension"
        raise ValueError(msg)
    return sum(float(x) * float(y) for x, y in zip(a, b, strict=True))


def orthogonal_pairs() -> list[tuple[str, str]]:
    """Return all vector-name pairs whose dot product is zero."""
    out: list[tuple[str, str]] = []
    for name_a, name_b in combinations(VECTORS.keys(), 2):
        if dot(VECTORS[name_a], VECTORS[name_b]) == 0.0:
            out.append((name_a, name_b))
    return out


def all_pairwise_dot_products() -> dict[tuple[str, str], float]:
    """Return dot products for each unordered pair of given vectors."""
    return {
        (name_a, name_b): dot(VECTORS[name_a], VECTORS[name_b])
        for name_a, name_b in combinations(VECTORS.keys(), 2)
    }
