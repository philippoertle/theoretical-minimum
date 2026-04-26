"""Interlude 1, Exercise 2 - vector subtraction rule.

Markdown copy (linked from the repo README):
``docs/book1/lecture-01/interlude-01/exercise-02.md``.

For vectors represented as equal-length coordinate lists/tuples:

- ``a - b`` is componentwise subtraction.
- Equivalently, ``a - b = a + (-b)``.
"""

from __future__ import annotations

from collections.abc import Sequence


def _require_same_dimension(a: Sequence[float], b: Sequence[float]) -> None:
    if len(a) != len(b):
        msg = "vectors must have the same dimension"
        raise ValueError(msg)


def vector_add(a: Sequence[float], b: Sequence[float]) -> tuple[float, ...]:
    """Return componentwise sum of two vectors."""
    _require_same_dimension(a, b)
    return tuple(float(x) + float(y) for x, y in zip(a, b, strict=True))


def vector_negate(v: Sequence[float]) -> tuple[float, ...]:
    """Return additive inverse of vector ``v``."""
    return tuple(-float(x) for x in v)


def vector_subtract(a: Sequence[float], b: Sequence[float]) -> tuple[float, ...]:
    """Return componentwise vector subtraction ``a - b``."""
    _require_same_dimension(a, b)
    return tuple(float(x) - float(y) for x, y in zip(a, b, strict=True))
