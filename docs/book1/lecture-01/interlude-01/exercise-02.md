# Book 1 — Lecture 1, Interlude 1, Exercise 2

Written notes for this exercise. Helper code lives in
[`exercise_02.py`](../../../../src/theoretical_minimum/book1/lecture_01/interlude_01/exercise_02.py).

## Prompt

Work out the rule for vector subtraction.

## Rule

Vector subtraction is defined componentwise:

$$
\mathbf{A}-\mathbf{B}=(A_1-B_1,\dots,A_n-B_n).
$$

Equivalent and often more useful form:

$$
\mathbf{A}-\mathbf{B}=\mathbf{A}+(-\mathbf{B}),
$$

where $-\mathbf{B}$ is the additive inverse of $\mathbf{B}$.

## Geometric interpretation

- If vectors share the same tail, $\mathbf{A}-\mathbf{B}$ is the vector from the
  tip of $\mathbf{B}$ to the tip of $\mathbf{A}$.
- In 2D/3D drawings, this is the same as adding $\mathbf{A}$ to the reversed
  arrow $-\mathbf{B}$.

## Quick check in 2D

$$
(3,-1)-(2,4)=(3-2,-1-4)=(1,-5).
$$

## Example drawing (GitHub preview)

The figure below visualizes the same 2D example with
$\mathbf{A}=(3,-1)$, $\mathbf{B}=(2,4)$, and $\mathbf{A}-\mathbf{B}=(1,-5)$.
The dashed red arrow shows the "tip of $\mathbf{B}$ to tip of $\mathbf{A}$"
interpretation.

![Vector subtraction example](./exercise-02-vector-subtraction.png)
