# Book 1 — Lecture 1, Interlude 1, Exercise 1

Written notes for this exercise. Plotting code and function definitions live in
[`exercise_01.py`](../../../../src/theoretical_minimum/book1/lecture_01/interlude_01/exercise_01.py).

## Prompt

Using a graphing calculator or a program like Mathematica, plot each of the
following functions:

$$
\begin{aligned}
f(t) &= t^4 + 3t^3 - 12t^2 + t - 6, \\
g(x) &= \sin(x) - \cos(x), \\
\theta(\alpha) &= e^\alpha + \alpha\ln(\alpha), \\
x(t) &= \sin^2(t) - \cos(t).
\end{aligned}
$$

## Notes before plotting

- $\theta(\alpha)$ is only defined for $\alpha>0$ because $\ln(\alpha)$ needs a
  positive argument.
- $f(t)$ is a quartic polynomial, so it grows to $+\infty$ for large positive
  and negative $t$.
- $g(x)$ and $x(t)$ are bounded oscillatory functions built from sine/cosine.

## Example plotting windows

Reasonable first windows:

- $t\in[-4,4]$ for $f(t)$
- $x\in[-2\pi,2\pi]$ for $g(x)$
- $\alpha\in[0.05,4]$ for $\theta(\alpha)$ (avoid $\alpha=0$)
- $t\in[-2\pi,2\pi]$ for $x(t)$

These are only starting points; zooming in/out helps identify turning points and
overall behavior.
