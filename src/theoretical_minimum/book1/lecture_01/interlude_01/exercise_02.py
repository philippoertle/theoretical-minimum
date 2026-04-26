"""Interlude 1, Exercise 2 - vector subtraction rule.

Markdown copy (linked from the repo README):
``docs/book1/lecture-01/interlude-01/exercise-02.md``.

For vectors represented as equal-length coordinate lists/tuples:

- ``a - b`` is componentwise subtraction.
- Equivalently, ``a - b = a + (-b)``.
"""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path


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


def save_vector_subtraction_example_png(
    path: str | Path,
    a: Sequence[float] = (3.0, -1.0),
    b: Sequence[float] = (2.0, 4.0),
) -> Path:
    """Save a 2D vector-subtraction example drawing and return the saved path."""
    if len(a) != 2 or len(b) != 2:
        msg = "example plot only supports 2D vectors"
        raise ValueError(msg)

    try:
        import matplotlib.pyplot as plt
    except ImportError as exc:
        msg = "plotting requires matplotlib; install it to render vector drawings"
        raise ImportError(msg) from exc

    ax_a, ay_a = float(a[0]), float(a[1])
    bx_b, by_b = float(b[0]), float(b[1])
    sx, sy = vector_subtract((ax_a, ay_a), (bx_b, by_b))

    fig, ax = plt.subplots(figsize=(6, 6), constrained_layout=True)

    # Vectors from origin.
    ax.arrow(0, 0, ax_a, ay_a, head_width=0.18, length_includes_head=True, color="tab:blue")
    ax.arrow(0, 0, bx_b, by_b, head_width=0.18, length_includes_head=True, color="tab:orange")
    ax.arrow(0, 0, sx, sy, head_width=0.18, length_includes_head=True, color="tab:green")

    # Difference as "tip(b) -> tip(a)".
    ax.arrow(bx_b, by_b, sx, sy, head_width=0.14, length_includes_head=True, color="tab:red", linestyle="--")

    ax.text(ax_a + 0.1, ay_a + 0.1, "a", color="tab:blue")
    ax.text(bx_b + 0.1, by_b + 0.1, "b", color="tab:orange")
    ax.text(sx + 0.1, sy + 0.1, "a-b", color="tab:green")
    ax.text(bx_b + sx / 2, by_b + sy / 2, "from tip(b) to tip(a)", color="tab:red")

    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.grid(True, alpha=0.3)
    ax.set_aspect("equal", adjustable="box")
    ax.set_title("Vector subtraction example: a=(3,-1), b=(2,4)")
    ax.set_xlim(-1.5, 4.5)
    ax.set_ylim(-6.0, 5.5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    target = Path(path).expanduser().resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(target, dpi=180)
    return target
