"""Interlude 1, Exercise 4 - magnitudes, dot product, and angle between vectors.

TeX/PDF write-up (linked from the repo README):
``docs/book1/lecture-01/interlude-01/exercise-04.tex``,
``docs/book1/lecture-01/interlude-01/exercise-04.pdf``.
"""

from __future__ import annotations

import math
from collections.abc import Sequence

VECTOR_A: tuple[float, float, float] = (2.0, -3.0, 1.0)
VECTOR_B: tuple[float, float, float] = (-4.0, -3.0, 2.0)


def dot(a: Sequence[float], b: Sequence[float]) -> float:
    """Return Euclidean dot product of vectors ``a`` and ``b``."""
    if len(a) != len(b):
        msg = "vectors must have the same dimension"
        raise ValueError(msg)
    return sum(float(x) * float(y) for x, y in zip(a, b, strict=True))


def magnitude(v: Sequence[float]) -> float:
    """Return Euclidean magnitude ||v||."""
    return math.sqrt(dot(v, v))


def angle_between_radians(a: Sequence[float], b: Sequence[float]) -> float:
    """Return angle between non-zero vectors ``a`` and ``b`` in radians."""
    ma = magnitude(a)
    mb = magnitude(b)
    if ma == 0.0 or mb == 0.0:
        msg = "angle undefined for zero vector"
        raise ValueError(msg)
    cosine = dot(a, b) / (ma * mb)
    cosine = max(-1.0, min(1.0, cosine))
    return math.acos(cosine)


def angle_between_degrees(a: Sequence[float], b: Sequence[float]) -> float:
    """Return angle between non-zero vectors ``a`` and ``b`` in degrees."""
    return math.degrees(angle_between_radians(a, b))


def exercise_values() -> dict[str, float]:
    """Compute requested values for Exercise 4 vectors A and B."""
    return {
        "magnitude_a": magnitude(VECTOR_A),
        "magnitude_b": magnitude(VECTOR_B),
        "dot_ab": dot(VECTOR_A, VECTOR_B),
        "angle_rad": angle_between_radians(VECTOR_A, VECTOR_B),
        "angle_deg": angle_between_degrees(VECTOR_A, VECTOR_B),
    }
