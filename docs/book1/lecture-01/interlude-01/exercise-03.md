# Book 1 — Lecture 1, Interlude 1, Exercise 3

Written notes for this exercise. Helper code lives in
[`exercise_03.py`](../../../../src/theoretical_minimum/book1/lecture_01/interlude_01/exercise_03.py).

## Prompt

Show that the magnitude of a vector satisfies:

$$
\lVert\mathbf{A}\rVert^2 = \mathbf{A}\cdot\mathbf{A}.
$$

## Proof in components

Let
$$
\mathbf{A} = (A_1, A_2, \dots, A_n).
$$

By definition of Euclidean magnitude,
$$
\lVert\mathbf{A}\rVert = \sqrt{A_1^2 + A_2^2 + \cdots + A_n^2}.
$$

Squaring both sides gives
$$
\lVert\mathbf{A}\rVert^2 = A_1^2 + A_2^2 + \cdots + A_n^2.
$$

By definition of the dot product,
$$
\mathbf{A}\cdot\mathbf{A} =
(A_1, \dots, A_n)\cdot(A_1, \dots, A_n)
= A_1^2 + \cdots + A_n^2.
$$

Therefore,
$$
\lVert \mathbf{A} \rVert^2 = \mathbf{A}\cdot\mathbf{A}.
$$

## Example

For $\mathbf{A}=(3,-4,12)$:
$$
\mathbf{A}\cdot\mathbf{A}=3^2+(-4)^2+12^2=169,\qquad
\lVert\mathbf{A}\rVert=13,\qquad
\lVert\mathbf{A}\rVert^2=169.
$$
