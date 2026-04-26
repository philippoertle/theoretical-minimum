# Theoretical Minimum — exercise solutions

This repository collects **code snippets and small programs** for working through the exercises in Leonard Susskind’s *The Theoretical Minimum* book series, as presented on the [official site](https://theoreticalminimum.com/).

Coverage is intended to span the full four-book sequence; work here begins with **classical mechanics**, aligned with:

- **Course:** [Classical Mechanics (Fall 2011)](https://theoreticalminimum.com/courses/classical-mechanics/2011/fall) — lecture list, iTunes/YouTube playlists  
- **Book:** [*The Theoretical Minimum: What You Need to Know to Start Doing Physics*](https://www.amazon.com/gp/product/046502811X) (Amazon product page)

The goal is not to replace the books or lectures, but to provide reproducible, checkable computations where exercises benefit from symbolic or numerical work, plus short written notes where an exercise is conceptual.

## Written solutions (Markdown)

- **Book 1, Lecture 1, Exercise 1** — [Closed vs open systems](docs/book1/lecture-01/exercise-01.md)
- **Book 1, Lecture 1, Exercise 2** — [Classifying six-state (die) laws](docs/book1/lecture-01/exercise-02.md)
- **Book 1, Lecture 1, Exercise 3** — [Allowable laws on the integer line](docs/book1/lecture-01/exercise-03.md)

## Math in Markdown (GitHub style)

To keep equations readable on GitHub, use TeX math delimiters consistently:

- Inline math: `$...$` (example: `$N_{n+1}=N_n+1$`)
- Display math blocks: `$$...$$`

Preferred notation:

- Use TeX forms like `\mathbb{Z}`, `N_{n+1}`, `N_n`, `n^2`, `(-1)^{N_n}`.
- Use TeX arrows in math mode, e.g. `\to`, `\leftrightarrow`, `\mapsto`.
- Avoid Unicode math symbols in source (`ℤ`, `→`, `−`, `²`) to prevent renderer/font ambiguity.

Practical tip:

- Keep long equations in standalone display blocks, and use inline math for short expressions in prose/tables.
