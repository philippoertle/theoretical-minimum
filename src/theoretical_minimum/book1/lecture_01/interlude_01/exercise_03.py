"""Interlude 1, Exercise 3 - show ||A||^2 = A·A.

TeX/PDF write-up (linked from the repo README):
``docs/book1/lecture-01/interlude-01/exercise-03.tex``,
``docs/book1/lecture-01/interlude-01/exercise-03.pdf``.
"""

from __future__ import annotations

import math
from collections.abc import Sequence


def dot(a: Sequence[float], b: Sequence[float]) -> float:
    """Return Euclidean dot product of vectors ``a`` and ``b``."""
    if len(a) != len(b):
        msg = "vectors must have the same dimension"
        raise ValueError(msg)
    return sum(float(x) * float(y) for x, y in zip(a, b, strict=True))


def magnitude(a: Sequence[float]) -> float:
    """Return Euclidean magnitude ||a||."""
    return math.sqrt(dot(a, a))


def magnitude_squared_equals_self_dot(a: Sequence[float], tol: float = 1e-12) -> bool:
    """Numerically check identity: ``||a||^2 == a·a`` within tolerance."""
    return abs(magnitude(a) ** 2 - dot(a, a)) <= tol
