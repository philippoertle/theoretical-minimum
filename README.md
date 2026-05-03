# Theoretical Minimum — exercise solutions

This repository collects **code snippets and small programs** for working through the exercises in Leonard Susskind’s *The Theoretical Minimum* book series, as presented on the [official site](https://theoreticalminimum.com/).

Coverage is intended to span the full four-book sequence; work here begins with **classical mechanics**, aligned with:

- **Course:** [Classical Mechanics (Fall 2011)](https://theoreticalminimum.com/courses/classical-mechanics/2011/fall) — lecture list, iTunes/YouTube playlists  
- **Book:** [*The Theoretical Minimum: What You Need to Know to Start Doing Physics*](https://www.amazon.com/gp/product/046502811X) (Amazon product page)

Exercise folders use the book’s lecture and interlude numbering. Unit titles (Book 1):

- **Lecture 1** — The Nature of Classical Physics  
- **Interlude 1** — Spaces, Trigonometry, and Vectors  
- **Lecture 2** — Motion  
- **Interlude 2** — Integral Calculus  

The goal is not to replace the books or lectures, but to provide reproducible, checkable computations where exercises benefit from symbolic or numerical work, plus short written notes where an exercise is conceptual.

## Written solutions

- **Book 1, Lecture 1, Exercise 1** — [Closed vs open systems (PDF)](docs/book1/lecture-01/exercise-01.pdf) ([TeX source](docs/book1/lecture-01/exercise-01.tex))
- **Book 1, Lecture 1, Exercise 2** — [Classifying six-state (die) laws (PDF)](docs/book1/lecture-01/exercise-02.pdf) ([TeX source](docs/book1/lecture-01/exercise-02.tex))
- **Book 1, Lecture 1, Exercise 3** — [Allowable laws on the integer line (PDF)](docs/book1/lecture-01/exercise-03.pdf) ([TeX source](docs/book1/lecture-01/exercise-03.tex))
- **Book 1, Lecture 1, Interlude 1, Exercise 1** — [Plotting four introductory functions (PDF)](docs/book1/lecture-01/interlude-01/exercise-01.pdf) ([TeX source](docs/book1/lecture-01/interlude-01/exercise-01.tex))
- **Book 1, Lecture 1, Interlude 1, Exercise 2** — [Vector subtraction rule (PDF)](docs/book1/lecture-01/interlude-01/exercise-02.pdf) ([TeX source](docs/book1/lecture-01/interlude-01/exercise-02.tex))
- **Book 1, Lecture 1, Interlude 1, Exercise 3** — [Why \|\|A\|\|^2 = A·A (PDF)](docs/book1/lecture-01/interlude-01/exercise-03.pdf) ([TeX source](docs/book1/lecture-01/interlude-01/exercise-03.tex))
- **Book 1, Lecture 1, Interlude 1, Exercise 4** — [Vector magnitudes, dot product, and angle (PDF)](docs/book1/lecture-01/interlude-01/exercise-04.pdf) ([TeX source](docs/book1/lecture-01/interlude-01/exercise-04.tex))
- **Book 1, Lecture 1, Interlude 1, Exercise 5** — [Orthogonal vector pair (PDF)](docs/book1/lecture-01/interlude-01/exercise-05.pdf) ([TeX source](docs/book1/lecture-01/interlude-01/exercise-05.tex))
- **Book 1, Lecture 1, Interlude 1, Exercise 6** — [Why orthogonal vectors have zero dot product (PDF)](docs/book1/lecture-01/interlude-01/exercise-06.pdf) ([TeX source](docs/book1/lecture-01/interlude-01/exercise-06.tex))
- **Book 1, Lecture 2, Exercise 1** — [Derivatives of four introductory functions (PDF)](docs/book1/lecture-02/exercise-01.pdf) ([TeX source](docs/book1/lecture-02/exercise-01.tex))
- **Book 1, Lecture 2, Exercise 2** — [Second derivatives of four introductory functions (PDF)](docs/book1/lecture-02/exercise-02.pdf) ([TeX source](docs/book1/lecture-02/exercise-02.tex))
- **Book 1, Lecture 2, Exercise 3** — [Chain rule for three composed functions (PDF)](docs/book1/lecture-02/exercise-03.pdf) ([TeX source](docs/book1/lecture-02/exercise-03.tex))
- **Book 1, Lecture 2, Exercise 4** — [Proving sum, product, and chain rules (PDF)](docs/book1/lecture-02/exercise-04.pdf) ([TeX source](docs/book1/lecture-02/exercise-04.tex))
- **Book 1, Lecture 2, Exercise 5** — [Derivatives of sin, cos, exp, and ln (PDF)](docs/book1/lecture-02/exercise-05.pdf) ([TeX source](docs/book1/lecture-02/exercise-05.tex))
- **Book 1, Lecture 2, Exercise 6** — [Period of simple harmonic motion (PDF)](docs/book1/lecture-02/exercise-06.pdf) ([TeX source](docs/book1/lecture-02/exercise-06.tex))
- **Book 1, Lecture 2, Exercise 7** — [Velocity and acceleration orthogonal in UCM (PDF)](docs/book1/lecture-02/exercise-07.pdf) ([TeX source](docs/book1/lecture-02/exercise-07.tex))
- **Book 1, Lecture 2, Exercise 8** — [Velocity, speed, acceleration for four plane curves (PDF)](docs/book1/lecture-02/exercise-08.pdf) ([TeX source](docs/book1/lecture-02/exercise-08.tex))

## Authoring and rendering workflow

Written solutions are maintained as `.tex` sources and committed `.pdf` outputs.
The PDF is the canonical rendered artifact for reading on GitHub.

- Keep notation and typography consistent across TeX files.
- Highlight `Prompt`, `Result`, and `Example` blocks in each exercise.
- Preserve source/compiled pairs in the same directory:
  - `exercise-XX.tex`
  - `exercise-XX.pdf`

To rebuild a PDF locally, run:

`pdflatex -interaction=nonstopmode -halt-on-error -output-directory "<target-dir>" "<path-to-tex-file>"`
