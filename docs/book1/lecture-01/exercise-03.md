# Book 1 — Lecture 1, Exercise 3

Written notes for this exercise. Small arithmetic checks live in
[`exercise_03.py`](../../../src/theoretical_minimum/book1/lecture_01/exercise_03.py).

## Prompt

Determine which of the dynamical laws shown in Eqs. (2) through (5) are
**allowable**. Equation (1), $N_{n+1}=N_n+1$, is already given as an
example of an allowable rule.

## What "allowable" means here

A law is **allowable** when it is:

1. **Deterministic**: the next state is fixed by the current state (a function
   $f$ from states to states).
2. **Reversible**: if you reverse every arrow, the rule is still deterministic;
   each state has exactly one predecessor as well as one successor. So $f$
   must be a bijection of the state space.

The setting is the infinite line of integer states $\mathbb{Z}$ (the same
picture used for the $+1$ step in Eq. (1)).

## The equations (as in the book)

Your prompt repeated $+1$ for Eq. (2); in the book, Eq. (2) is the downward
step, i.e. the reverse of Eq. (1):

$$
\begin{aligned}
(1)\quad &N_{n+1}=N_n+1 \\
(2)\quad &N_{n+1}=N_n-1 \\
(3)\quad &N_{n+1}=N_n+2 \\
(4)\quad &N_{n+1}=N_n^2 \\
(5)\quad &N_{n+1}=(-1)^{N_n}N_n
\end{aligned}
$$

For Eq. (5), interpret $(-1)^N$ using parity of the integer $N$:

- even $N \mapsto +1$,
- odd $N \mapsto -1$.

That matches the cycle picture in the text and extends naturally to negative
integers (e.g. $(-1)^{-3}=-1$).

## Verdicts

### (2) $N_{n+1}=N_n-1$ — **allowable**

This is Eq. (1) with time reversed (subtract instead of add). It is a
bijection $\mathbb{Z}\to\mathbb{Z}$ with inverse
$f(N)=N+1$ (equivalently, if forward is $f(N)=N-1$, then $f^{-1}(N)=N+1$).
So it is deterministic and reversible.

### (3) $N_{n+1}=N_n+2$ — **allowable**

Successor map $f(N)=N+2$ is a bijection with inverse $f^{-1}(N)=N-2$. The line
splits into two disjoint chains (evens and odds), each infinite in both
directions; within each chain the dynamics is reversible just like the $\pm 1$
step.

### (4) $N_{n+1}=N_n^2$ — **not allowable**

- **Not injective:** $2^2=(-2)^2=4$, so from $4$ you cannot uniquely recover
  the previous state; reversing the arrows is not deterministic.
- **Not surjective onto $\mathbb{Z}$:** many integers are not perfect squares
  (e.g. there is no integer $n$ with $n^2=2$), so some states are unreachable
  and there is no predecessor for them in a full $\mathbb{Z}$ model.

So Eq. (4) fails reversibility (and does not act as a permutation of
$\mathbb{Z}$).

### (5) $N_{n+1}=(-1)^{N_n}N_n$ — **allowable**

- If $N$ is even, $N\mapsto N$ (fixed point).
- If $N$ is odd, $N\mapsto -N$; applying again gives $-N\mapsto N$ (a 2-cycle
  between each odd pair $N,-N$).

Every integer has a unique predecessor:

- Even $m$: the only preimage is $m$ itself.
- Odd $m$: the only preimage is $-m$ (also odd).

So $f$ is a bijection of $\mathbb{Z}$; the law is deterministic and reversible.

## Short summary

| Equation | Allowable? |
|---|---|
| (2) $N_{n+1}=N_n-1$ | Yes |
| (3) $N_{n+1}=N_n+2$ | Yes |
| (4) $N_{n+1}=N_n^2$ | No |
| (5) $N_{n+1}=(-1)^{N_n}N_n$ | Yes |
