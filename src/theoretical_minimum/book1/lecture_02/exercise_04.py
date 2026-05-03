"""Lecture 2, Exercise 4 — proofs of sum, product, and chain rules.

TeX/PDF write-up:
``docs/book1/lecture-02/exercise-04.tex``,
``docs/book1/lecture-02/exercise-04.pdf``.

**Prompt (paraphrased).** Prove the sum rule, the product rule, and the chain rule
for derivatives.

---

**Sum rule.** For differentiable ``f`` and ``g`` at ``x``, write ``S = f + g``. The
Newton quotient splits: ``(S(x+h)-S(x))/h = (f(x+h)-f(x))/h + (g(x+h)-g(x))/h``.
Taking ``h → 0`` gives ``S'(x) = f'(x) + g'(x)``.

**Product rule.** For ``P = fg``, add and subtract ``f(x+h)g(x)``:
``P(x+h)-P(x) = f(x+h)(g(x+h)-g(x)) + g(x)(f(x+h)-f(x))``. Divide by ``h`` and let
``h → 0``, using continuity of ``f`` at ``x`` so ``f(x+h) → f(x)``, to obtain
``P'(x) = f(x)g'(x) + g(x)f'(x)``.

**Chain rule.** For ``F(x) = f(g(x))`` with ``g`` differentiable at ``x`` and ``f``
differentiable at ``g(x)``, define ``Q(h)`` as ``(f(g(x+h))-f(g(x)))/(g(x+h)-g(x))``
when ``g(x+h) ≠ g(x)``, and ``Q(h) = f'(g(x))`` when ``g(x+h) = g(x)``. Then
``(F(x+h)-F(x))/h = Q(h) · (g(x+h)-g(x))/h`` for all ``h ≠ 0``, and
``Q(h) → f'(g(x))``, ``(g(x+h)-g(x))/h → g'(x)``, hence ``F'(x) = f'(g(x)) g'(x)``.

The PDF also includes small TikZ figures (stacked secants, rectangle strips, and a
two-stage pipeline) to visualize the three rules.
"""
