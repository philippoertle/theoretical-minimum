"""Interlude 1, Exercise 6 - why orthogonal vectors have zero dot product.

TeX/PDF write-up (linked from the repo README):
``docs/book1/lecture-01/interlude-01/exercise-06.tex``,
``docs/book1/lecture-01/interlude-01/exercise-06.pdf``.
"""

from __future__ import annotations

import math
from collections.abc import Sequence


def dot(a: Sequence[int | float], b: Sequence[int | float]) -> float:
    """Return Euclidean dot product of vectors ``a`` and ``b``."""
    if len(a) != len(b):
        msg = "vectors must have the same dimension"
        raise ValueError(msg)
    return sum(float(x) * float(y) for x, y in zip(a, b, strict=True))


def magnitude(v: Sequence[int | float]) -> float:
    """Return Euclidean vector magnitude."""
    return math.sqrt(dot(v, v))


def angle_between_radians(a: Sequence[int | float], b: Sequence[int | float]) -> float:
    """Return angle in radians between non-zero vectors ``a`` and ``b``."""
    ma = magnitude(a)
    mb = magnitude(b)
    if ma == 0.0 or mb == 0.0:
        msg = "angle undefined for zero vector"
        raise ValueError(msg)
    cosine = dot(a, b) / (ma * mb)
    cosine = max(-1.0, min(1.0, cosine))
    return math.acos(cosine)


def is_orthogonal(a: Sequence[int | float], b: Sequence[int | float], tol: float = 1e-12) -> bool:
    """Return True iff vectors are orthogonal (dot product approximately zero)."""
    return abs(dot(a, b)) <= tol
