"""Lecture 2, Exercise 2 — second derivatives of four introductory functions.

TeX/PDF write-up:
``docs/book1/lecture-02/exercise-02.tex``,
``docs/book1/lecture-02/exercise-02.pdf``.

Same four functions as ``exercise_01``; here we return the second derivative with
respect to each function's natural independent variable.
"""

from __future__ import annotations

import math


def d2f_dt2(t: float) -> float:
    """Return ``f''(t)`` for ``f(t) = t^4 + 3t^3 - 12t^2 + t - 6``."""
    return 12 * t**2 + 18 * t - 24


def d2g_dx2(x: float) -> float:
    """Return ``g''(x)`` for ``g(x) = sin(x) - cos(x)``."""
    return -math.sin(x) + math.cos(x)


def d2theta_dalpha2(alpha: float) -> float:
    """Return ``theta''(alpha)`` for ``theta(alpha) = exp(alpha) + alpha*log(alpha)``.

    Domain requires ``alpha > 0`` because of ``log(alpha)`` and ``1/alpha``.
    """
    if alpha <= 0:
        msg = (
            "alpha must be > 0 because log(alpha) and 1/alpha are undefined for non-positive alpha"
        )
        raise ValueError(msg)
    return math.exp(alpha) + 1 / alpha


def d2x_dt2(t: float) -> float:
    """Return ``x''(t)`` for ``x(t) = sin(t)^2 - cos(t)``."""
    return 2 * math.cos(2 * t) + math.cos(t)
