# Book 1 — Lecture 1, Exercise 2

Written notes for this exercise. Executable checks and the encoded examples
live in
[`exercise_02.py`](../../../src/theoretical_minimum/book1/lecture_01/exercise_02.py).

## Prompt

Can you think of a general way to classify the laws that are possible for a
six-state system?

**Setup.** Here the six states are the faces of a die. A *dynamical law* says,
deterministically, which state follows each state.

## What kind of “laws” the examples use

In all four textbook examples, each state has **exactly one** successor **and**
exactly one predecessor. The update rule is therefore a **bijection** of the six
labels: a **permutation**. That is the usual “information-preserving” situation
emphasized when discussing reversible evolution on a finite configuration space.

If you dropped bijectivity and only required “one successor per state,” you would
allow **non-invertible** rules (several states might map to the same next
state). Those are still legitimate deterministic laws, but their classification
uses **directed functional graphs** (cycles with trees feeding into them), not
plain cycle decompositions of permutations. The rest of this note matches the
four given examples and the reversible setting.

## General classification (reversible / permutation laws)

Any permutation of six objects splits uniquely into **disjoint cycles**. The
**cycle type** is the multiset of those cycle lengths. It is customary to write
it as a **partition of 6**—positive integers that sum to 6, usually sorted in
**descending** order.

Two laws that differ only by **renaming** the states (relabeling the faces) have
the **same** cycle type. In group-theory language, these are the **conjugacy
classes** of the symmetric group \(S_6\).

So one clean answer to “classify the possible laws up to relabeling” is:

> **List all integer partitions of 6.** Each partition is one class of
> reversible six-state laws.

There are **11** such partitions:

| Partition | English description (cycle lengths) |
|-----------|-------------------------------------|
| (6) | one 6-cycle |
| (5, 1) | one 5-cycle and a fixed point |
| (4, 2) | a 4-cycle and a 2-cycle |
| (4, 1, 1) | a 4-cycle and two fixed points |
| (3, 3) | two 3-cycles |
| (3, 2, 1) | a 3-cycle, a 2-cycle, and a fixed point |
| (3, 1, 1, 1) | one 3-cycle and three fixed points |
| (2, 2, 2) | three 2-cycles |
| (2, 2, 1, 1) | two 2-cycles and two fixed points |
| (2, 1, 1, 1, 1) | one 2-cycle and four fixed points |
| (1, 1, 1, 1, 1, 1) | identity; every state fixed |

## The four examples

| Example | Cycle type (partition) | Structure |
|---------|-------------------------|-----------|
| $1\to2\to3\to4\to5\to6\to1$ | (6) | single 6-cycle |
| $1\to3\to2\to6\to4\to5\to1$ | (6) | single 6-cycle (different ordering) |
| $1\to2\to6\to1$ and $3\to4\to5\to3$ | (3, 3) | two 3-cycles |
| $1\to1$; $5\leftrightarrow6$; $2\to3\to4\to2$ | (3, 2, 1) | 3-cycle, 2-cycle, fixed point |

Examples 1 and 2 are the **same class**—both are long 6-cycles—even though the
arrows visit labels in a different order.

## Takeaway

For a **six-state die** with a **reversible** deterministic law, the natural
invariant is the **partition of 6** given by **cycle lengths**. Counting
**distinct laws with labeled faces** is a different (much larger) question
(\(6! = 720\) permutations total); the partition counts **equivalence classes**
under relabeling.
