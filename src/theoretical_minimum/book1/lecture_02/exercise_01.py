"""Lecture 2, Exercise 1 — derivatives of four introductory functions.

TeX/PDF write-up:
``docs/book1/lecture-02/exercise-01.tex``,
``docs/book1/lecture-02/exercise-01.pdf``.

These are the same four functions introduced in Lecture 1 / Interlude 1 /
Exercise 1 for plotting; here we differentiate them.

- ``f(t) = t^4 + 3t^3 - 12t^2 + t - 6``
- ``g(x) = sin(x) - cos(x)``
- ``theta(alpha) = exp(alpha) + alpha*log(alpha)`` for ``alpha > 0``
- ``x(t) = sin(t)^2 - cos(t)``
"""

from __future__ import annotations

import math


def df_dt(t: float) -> float:
    """Return ``f'(t)`` for ``f(t) = t^4 + 3t^3 - 12t^2 + t - 6``."""
    return 4 * t**3 + 9 * t**2 - 24 * t + 1


def dg_dx(x: float) -> float:
    """Return ``g'(x)`` for ``g(x) = sin(x) - cos(x)``."""
    return math.cos(x) + math.sin(x)


def dtheta_dalpha(alpha: float) -> float:
    """Return ``theta'(alpha)`` for ``theta(alpha) = exp(alpha) + alpha*log(alpha)``.

    Domain requires ``alpha > 0`` because of ``log(alpha)``.
    """
    if alpha <= 0:
        msg = "alpha must be > 0 because log(alpha) is undefined for non-positive alpha"
        raise ValueError(msg)
    return math.exp(alpha) + math.log(alpha) + 1


def dx_dt(t: float) -> float:
    """Return ``x'(t)`` for ``x(t) = sin(t)^2 - cos(t)``."""
    return math.sin(t) * (2 * math.cos(t) + 1)
