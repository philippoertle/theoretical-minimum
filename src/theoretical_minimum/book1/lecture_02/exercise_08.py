"""Lecture 2, Exercise 8 — velocity, speed, and acceleration for four plane curves.

TeX/PDF write-up:
``docs/book1/lecture-02/exercise-08.tex``,
``docs/book1/lecture-02/exercise-08.pdf``.

Parametric motions: (i) ``(cos ωt, e^{ωt})``, (ii) phased uniform circle,
(iii) astroid ``(c cos³t, c sin³t)``, (iv) cycloid ``(c(t−sin t), c(1−cos t))``.

The PDF includes TikZ sketches of each trajectory (plus sample position, velocity,
and acceleration arrows for uniform circular motion).
"""

from __future__ import annotations

import math
from typing import NamedTuple


class KinematicState(NamedTuple):
    """Position ``r``, velocity ``v``, scalar speed ``|v|``, acceleration ``a``."""

    position: tuple[float, float]
    velocity: tuple[float, float]
    speed: float
    acceleration: tuple[float, float]


def kinematic_cos_exp(*, omega: float, t: float) -> KinematicState:
    """(i) ``r = (cos(ωt), exp(ωt))``."""
    wt = omega * t
    x = math.cos(wt)
    y = math.exp(wt)
    vx = -omega * math.sin(wt)
    vy = omega * math.exp(wt)
    ax = -(omega**2) * math.cos(wt)
    ay = (omega**2) * math.exp(wt)
    speed = math.hypot(vx, vy)
    return KinematicState((x, y), (vx, vy), speed, (ax, ay))


def kinematic_phased_circle(*, omega: float, phi: float, t: float) -> KinematicState:
    """(ii) ``r = (cos(ωt − φ), sin(ωt − φ))`` — unit circle, constant speed ``|ω|``."""
    theta = omega * t - phi
    x = math.cos(theta)
    y = math.sin(theta)
    vx = -omega * math.sin(theta)
    vy = omega * math.cos(theta)
    ax = -(omega**2) * math.cos(theta)
    ay = -(omega**2) * math.sin(theta)
    speed = abs(omega)
    return KinematicState((x, y), (vx, vy), speed, (ax, ay))


def kinematic_astroid(*, c: float, t: float) -> KinematicState:
    """(iii) ``r = (c cos³t, c sin³t)``."""
    ct = math.cos(t)
    st = math.sin(t)
    x = c * ct**3
    y = c * st**3
    vx = -3.0 * c * ct**2 * st
    vy = 3.0 * c * st**2 * ct
    speed = 1.5 * abs(c) * abs(math.sin(2.0 * t))
    ax = 3.0 * c * ct * (2.0 * st**2 - ct**2)
    ay = 3.0 * c * st * (2.0 * ct**2 - st**2)
    return KinematicState((x, y), (vx, vy), speed, (ax, ay))


def kinematic_cycloid(*, c: float, t: float) -> KinematicState:
    """(iv) ``r = (c(t − sin t), c(1 − cos t))``."""
    x = c * (t - math.sin(t))
    y = c * (1.0 - math.cos(t))
    vx = c * (1.0 - math.cos(t))
    vy = c * math.sin(t)
    speed = 2.0 * abs(c) * abs(math.sin(0.5 * t))
    ax = c * math.sin(t)
    ay = c * math.cos(t)
    return KinematicState((x, y), (vx, vy), speed, (ax, ay))
