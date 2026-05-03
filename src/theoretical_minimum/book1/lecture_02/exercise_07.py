"""Lecture 2, Exercise 7 — velocity and acceleration orthogonal in uniform circular motion.

TeX/PDF write-up:
``docs/book1/lecture-02/exercise-07.tex``,
``docs/book1/lecture-02/exercise-07.pdf``.

**Prompt (paraphrased).** For planar components ``v_x, v_y`` (velocity) and ``a_x, a_y``
(acceleration) of uniform circular motion, show the corresponding vectors are orthogonal.

**Result.** ``v · a = 0`` for all ``t``. Also ``r · v = 0`` for ``r = (R cos(ωt), R sin(ωt))``.
"""

from __future__ import annotations

import math


def velocity_ucm(*, radius: float, omega: float, t: float) -> tuple[float, float]:
    """Return ``(v_x, v_y)`` for uniform circular motion with ``radius R > 0``."""
    if radius <= 0:
        msg = "radius must be positive"
        raise ValueError(msg)
    wt = omega * t
    return (-radius * omega * math.sin(wt), radius * omega * math.cos(wt))


def acceleration_ucm(*, radius: float, omega: float, t: float) -> tuple[float, float]:
    """Return ``(a_x, a_y)`` matching the exercise's acceleration components."""
    if radius <= 0:
        msg = "radius must be positive"
        raise ValueError(msg)
    wt = omega * t
    return (-radius * omega**2 * math.cos(wt), -radius * omega**2 * math.sin(wt))


def position_ucm(*, radius: float, omega: float, t: float) -> tuple[float, float]:
    """Return ``(x, y)`` for ``r = R(cos ωt, sin ωt)``."""
    if radius <= 0:
        msg = "radius must be positive"
        raise ValueError(msg)
    wt = omega * t
    return (radius * math.cos(wt), radius * math.sin(wt))


def dot(a: tuple[float, float], b: tuple[float, float]) -> float:
    """Return the dot product ``a · b``."""
    return a[0] * b[0] + a[1] * b[1]


def velocity_acceleration_dot(*, radius: float, omega: float, t: float) -> float:
    """Return ``v · a`` for the exercise's uniform circular motion."""
    return dot(
        velocity_ucm(radius=radius, omega=omega, t=t),
        acceleration_ucm(radius=radius, omega=omega, t=t),
    )


def position_velocity_dot(*, radius: float, omega: float, t: float) -> float:
    """Return ``r · v`` for ``r = R(cos ωt, sin ωt)`` and the matching velocity."""
    return dot(
        position_ucm(radius=radius, omega=omega, t=t),
        velocity_ucm(radius=radius, omega=omega, t=t),
    )
