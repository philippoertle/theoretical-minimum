"""Lecture 2, Exercise 5 — derivatives of sin, cos, exp, and ln from first principles.

TeX/PDF write-up:
``docs/book1/lecture-02/exercise-05.tex``,
``docs/book1/lecture-02/exercise-05.pdf``.

**Prompt (paraphrased).** Prove
``d(sin(t))/dt = cos(t)``, ``d(cos(t))/dt = -sin(t)``, ``d(e^t)/dt = e^t``,
``d(ln(t))/dt = 1/t`` (for ``t > 0`` in the logarithm), using trigonometric identities
and limit properties.

---

**Sine / cosine.** Expand ``sin(t+h)`` and ``cos(t+h)`` with angle-addition formulas,
divide by ``h``, and use ``(sin h)/h → 1`` and ``(cos h - 1)/h → 0`` (the latter from
``1 - cos h = 2 sin^2(h/2)``).

**Exponential.** Factor ``e^t`` from ``(e^{t+h} - e^t)/h`` and use ``(e^h - 1)/h → 1``.

**Logarithm.** Write ``(ln(t+h) - ln(t))/h = (1/t) · (ln(1+u)/u)`` with ``u = h/t``;
relate ``ln(1+u)/u`` to ``v/(e^v - 1)`` with ``v = ln(1+u)`` and the same exponential
limit to get ``1/t``.

The PDF includes TikZ figures (unit circle, sine/cosine/exponential/logarithm secants)
alongside the algebra.
"""
