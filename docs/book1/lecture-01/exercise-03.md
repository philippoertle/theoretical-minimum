# Book 1 — Lecture 1, Exercise 3

Written notes for this exercise. Small arithmetic checks live in
[`exercise_03.py`](../../../src/theoretical_minimum/book1/lecture_01/exercise_03.py).

## Prompt

Determine which of the dynamical laws shown in Eqs. (2) through (5) are
**allowable**. Equation (1), **N(n+1) = N(n) + 1**, is already given as an
example of an allowable rule.

## What “allowable” means here

A law is **allowable** when it is:

1. **Deterministic** — the next state is fixed by the current state (a function
   **f** from states to states).
2. **Reversible** — if you reverse every arrow, the rule is still deterministic:
   each state has **exactly one** predecessor as well as one successor. So **f**
   must be a **bijection** of the state space.

The setting is the **infinite line of integer states** **ℤ** (the same picture
used for the +1 step in Eq. (1)).

## The equations (as in the book)

Your prompt repeated +1 for Eq. (2); in the book, **(2)** is the **downward**
step, i.e. the reverse of (1):

| Eq. | Law |
|-----|-----|
| (1) | **N(n+1) = N(n) + 1** (example: allowable) |
| (2) | **N(n+1) = N(n) − 1** |
| (3) | **N(n+1) = N(n) + 2** |
| (4) | **N(n+1) = N(n)²** |
| (5) | **N(n+1) = (−1)^N(n) N(n)** |

For (5), interpret **(−1)^N** using the parity of the **integer** **N** (even →
+1, odd → −1). That matches the cycle picture in the text and extends sensibly
to negative **N** (e.g. **(−1)⁻³ = −1** in the usual real sense).

## Verdicts

### (2) N(n+1) = N(n) − 1 — **allowable**

This is Eq. (1) with **time reversed** (subtract instead of add). It is a
bijection **ℤ → ℤ** with inverse **N ↦ N + 1**. Deterministic and reversible.

### (3) N(n+1) = N(n) + 2 — **allowable**

Successor map **f(N) = N + 2** is a bijection with inverse **N ↦ N − 2**. The
line splits into **two** disjoint “chains” (evens and odds), each infinite in
both directions; within each chain the dynamics is reversible just like the ±1
step.

### (4) N(n+1) = N(n)² — **not allowable**

- **Not injective:** **2² = (−2)² = 4**, so from **4** you cannot uniquely recover
  the previous state — reversing the arrows is not deterministic.
- **Not surjective onto ℤ:** many integers are not perfect squares (e.g. there is
  no integer **n** with **n² = 2**), so some states are unreachable and there is
  no predecessor for them in a full **ℤ** model.

So (4) fails **reversibility** (and does not act as a permutation of **ℤ**).

### (5) N(n+1) = (−1)^N N — **allowable**

- If **N** is **even**, **N ↦ N** (fixed point).
- If **N** is **odd**, **N ↦ −N**; applying again gives **−N ↦ N** (a 2-cycle
  between each odd **N** and **−N**).

Every integer has a unique predecessor:

- Even **m**: the only preimage is **m** itself.
- Odd **m**: the only preimage is **−m** (also odd).

So **f** is a bijection of **ℤ**; the law is deterministic and reversible.

## Short summary

| Equation | Allowable? |
|----------|------------|
| (2) N − 1 | Yes |
| (3) N + 2 | Yes |
| (4) N² | No |
| (5) (−1)^N N | Yes |
