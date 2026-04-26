"""Interlude 1, Exercise 1 - plot four introductory functions.

Markdown copy (linked from the repo README):
``docs/book1/lecture-01/interlude-01/exercise-01.md``.

Functions from the prompt:

- ``f(t) = t^4 + 3t^3 - 12t^2 + t - 6``
- ``g(x) = sin(x) - cos(x)``
- ``theta(alpha) = exp(alpha) + alpha*log(alpha)`` (domain: ``alpha > 0``)
- ``x(t) = sin(t)^2 - cos(t)``

The plotting helper imports matplotlib lazily so this module remains usable even
when plotting dependencies are not installed.
"""

from __future__ import annotations

import math


def f_of_t(t: float) -> float:
    """Return ``f(t) = t^4 + 3t^3 - 12t^2 + t - 6``."""
    return t**4 + 3 * t**3 - 12 * t**2 + t - 6


def g_of_x(x: float) -> float:
    """Return ``g(x) = sin(x) - cos(x)``."""
    return math.sin(x) - math.cos(x)


def theta_of_alpha(alpha: float) -> float:
    """Return ``theta(alpha) = exp(alpha) + alpha*log(alpha)`` for ``alpha > 0``."""
    if alpha <= 0:
        msg = "alpha must be > 0 because log(alpha) is undefined for non-positive alpha"
        raise ValueError(msg)
    return math.exp(alpha) + alpha * math.log(alpha)


def x_of_t(t: float) -> float:
    """Return ``x(t) = sin(t)^2 - cos(t)``."""
    return math.sin(t) ** 2 - math.cos(t)


def plot_prompt_functions() -> None:
    """Plot all four prompt functions in a 2x2 figure.

    Raises:
        ImportError: If matplotlib or numpy is not installed.
    """
    try:
        import matplotlib.pyplot as plt
        import numpy as np
    except ImportError as exc:
        msg = "plotting requires matplotlib and numpy; install them to render graphs"
        raise ImportError(msg) from exc

    t_poly = np.linspace(-4.0, 4.0, 800)
    x_trig = np.linspace(-2.0 * np.pi, 2.0 * np.pi, 800)
    alpha = np.linspace(0.05, 4.0, 800)
    t_mix = np.linspace(-2.0 * np.pi, 2.0 * np.pi, 800)

    fig, axes = plt.subplots(2, 2, figsize=(11, 8), constrained_layout=True)

    axes[0, 0].plot(t_poly, [f_of_t(float(t)) for t in t_poly], color="tab:blue")
    axes[0, 0].set_title(r"$f(t)=t^4+3t^3-12t^2+t-6$")
    axes[0, 0].set_xlabel("t")
    axes[0, 0].grid(True, alpha=0.3)

    axes[0, 1].plot(x_trig, [g_of_x(float(x)) for x in x_trig], color="tab:orange")
    axes[0, 1].set_title(r"$g(x)=\sin(x)-\cos(x)$")
    axes[0, 1].set_xlabel("x")
    axes[0, 1].grid(True, alpha=0.3)

    axes[1, 0].plot(
        alpha,
        [theta_of_alpha(float(a)) for a in alpha],
        color="tab:green",
    )
    axes[1, 0].set_title(r"$\theta(\alpha)=e^\alpha+\alpha\ln(\alpha)$")
    axes[1, 0].set_xlabel(r"$\alpha$")
    axes[1, 0].grid(True, alpha=0.3)

    axes[1, 1].plot(t_mix, [x_of_t(float(t)) for t in t_mix], color="tab:red")
    axes[1, 1].set_title(r"$x(t)=\sin^2(t)-\cos(t)$")
    axes[1, 1].set_xlabel("t")
    axes[1, 1].grid(True, alpha=0.3)

    fig.suptitle("Book 1 / Lecture 1 / Interlude 1 / Exercise 1", fontsize=12)
    plt.show()


if __name__ == "__main__":
    plot_prompt_functions()
