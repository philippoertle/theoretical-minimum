"""Lecture 2, Exercise 6 — period of simple harmonic motion.

TeX/PDF write-up:
``docs/book1/lecture-02/exercise-06.tex``,
``docs/book1/lecture-02/exercise-06.pdf``.

**Prompt (paraphrased).** How long does one full cycle of SHM take?

**Result.** With angular frequency ``omega > 0``, the period is ``T = 2 * pi / omega``.
For an ideal spring--mass system, ``omega = sqrt(k/m)``, so ``T = 2 * pi * sqrt(m/k)``.
"""

from __future__ import annotations

import math


def period_from_angular_frequency(omega: float) -> float:
    """Return the SHM period ``T = 2*pi/omega`` for ``omega > 0`` (radians per unit time)."""
    if omega <= 0:
        msg = "omega must be positive for a physical oscillation period"
        raise ValueError(msg)
    return 2 * math.pi / omega


def period_spring_mass(*, mass_kg: float, spring_constant: float) -> float:
    """Return ``T = 2*pi*sqrt(m/k)`` for an ideal spring--mass oscillator.

    ``mass_kg`` is the mass ``m`` (kg) and ``spring_constant`` is ``k`` (N/m).
    """
    if mass_kg <= 0:
        msg = "mass_kg must be positive"
        raise ValueError(msg)
    if spring_constant <= 0:
        msg = "spring_constant k must be positive"
        raise ValueError(msg)
    return 2 * math.pi * math.sqrt(mass_kg / spring_constant)
