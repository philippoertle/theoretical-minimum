"""Exercise 3 - Which discrete laws on the integers are *allowable*?

Markdown copy (linked from the repo README): ``docs/book1/lecture-01/exercise-03.md``.

In Lecture 1 / this chapter, a dynamical law ``N(n+1) = f(N(n))`` on the integer
line is **allowable** when it is:

1. **Deterministic** - each state has exactly one successor (a function
   ``f : Z -> Z``).
2. **Reversible** - each state has exactly one predecessor (the same law read
   backward is deterministic), so ``f`` is a **bijection** of ``Z``.

Equation (1) is ``N(n+1) = N(n) - 1`` (the "minus-one" step). We evaluate
Eqs. (2)-(5) against the allowable criteria.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Final, TypeAlias

IntMap: TypeAlias = Callable[[int], int]

# Book equations (2)-(5) for integer state N(n) in Z.


def step_eq2_plus_one(n: int) -> int:
    """Eq. (2): N(n+1) = N(n) + 1."""
    return n + 1


def step_eq3_plus_two(n: int) -> int:
    """Eq. (3): N(n+1) = N(n) + 2."""
    return n + 2


def step_eq4_square(n: int) -> int:
    """Eq. (4): N(n+1) = N(n)^2."""
    return n * n


def step_eq5_sign_flip(n: int) -> int:
    """Eq. (5): N(n+1) = (-1)^{N(n)} N(n), using parity on Z.

    For integer *n*, (-1)^n is +1 if *n* is even and -1 if *n* is odd (parity
    via ``n % 2`` agrees with this for negative integers in Python).
    """
    sign = 1 if n % 2 == 0 else -1
    return sign * n


LAWS: Final[dict[str, IntMap]] = {
    "eq2_plus_one": step_eq2_plus_one,
    "eq3_plus_two": step_eq3_plus_two,
    "eq4_square": step_eq4_square,
    "eq5_sign_flip": step_eq5_sign_flip,
}


def square_law_collides_distinct_integers() -> tuple[int, int]:
    """Return two distinct integers that map to the same value under Eq. (4)."""
    return 2, -2


def integer_square_roots_of_two_exist() -> bool:
    """True iff some integer *n* satisfies *n² = 2*."""
    return any(n * n == 2 for n in range(-3, 4))


def preimage_eq5(m: int) -> int:
    """Unique integer *N* with *f(N) = m* for Eq. (5)."""
    if m % 2 == 0:
        return m
    return -m


def is_bijection_on_interval(f: IntMap, lo: int, hi: int) -> bool:
    """True if *f* restricts to a permutation of ``{lo, …, hi}``."""
    domain = list(range(lo, hi + 1))
    images = [f(n) for n in domain]
    return len(set(images)) == len(images) and set(images) == set(domain)


def eq5_is_bijection_on_symmetric_interval(radius: int) -> bool:
    """Sanity check: Eq. (5) permutes ``{-radius, …, radius}``."""
    return is_bijection_on_interval(step_eq5_sign_flip, -radius, radius)
