"""Lecture 2, Exercise 3 — chain-rule derivatives of three composed functions.

TeX/PDF write-up:
``docs/book1/lecture-02/exercise-03.tex``,
``docs/book1/lecture-02/exercise-03.pdf``.

- ``g(t) = sin(t^2) - cos(t^2)``
- ``theta(alpha) = exp(3*alpha) + 3*alpha*log(3*alpha)`` for ``alpha > 0``
- ``x(t) = sin(t^2)^2 - cos(t^2)``
"""

from __future__ import annotations

import math


def dg_dt(t: float) -> float:
    """Return ``g'(t)`` for ``g(t) = sin(t^2) - cos(t^2)``."""
    u = t * t
    return 2 * t * (math.cos(u) + math.sin(u))


def dtheta_dalpha(alpha: float) -> float:
    """Return ``theta'(alpha)`` for ``theta(alpha) = exp(3*alpha) + 3*alpha*log(3*alpha)``.

    Domain requires ``alpha > 0`` so ``log(3*alpha)`` is defined.
    """
    if alpha <= 0:
        msg = "alpha must be > 0 so that log(3*alpha) is defined"
        raise ValueError(msg)
    return 3 * math.exp(3 * alpha) + 3 * math.log(3 * alpha) + 3


def dx_dt(t: float) -> float:
    """Return ``x'(t)`` for ``x(t) = sin(t^2)^2 - cos(t^2)``."""
    u = t * t
    return 2 * t * math.sin(u) * (2 * math.cos(u) + 1)
