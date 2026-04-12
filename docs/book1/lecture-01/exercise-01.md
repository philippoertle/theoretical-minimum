# Book 1 — Lecture 1, Exercise 1

Written notes for this exercise. The same text lives as the module docstring in
[`exercise_01.py`](../../../src/theoretical_minimum/book1/lecture_01/exercise_01.py)
so it stays easy to find from Python tooling and tests.

## Prompt (paraphrased)

Since the notion is so important to theoretical physics, think about what a
closed system is and speculate on whether closed systems can actually exist.
What assumptions are implicit in establishing a closed system? What is an open
system?

## Closed system (working definition)

In theoretical physics, a *closed* system is one you describe with a *complete*
set of dynamical variables and *deterministic* (or, in quantum theory, unitary)
laws that involve *only* those variables. Nothing outside the model is allowed
to influence the state except through quantities you have already included.
Colloquially: no hidden taps of energy, momentum, or information from an
unmodeled environment.

## Implicit assumptions

Calling a system “closed” usually smuggles in several idealizations:

- **Exhaustive state:** You believe you have listed every degree of freedom that
  can matter for the question at hand on the relevant time and energy scales.
- **Known laws:** The equations of motion (or the Hamiltonian / Lagrangian) are
  taken to be *exact* for that full state—no extra stochastic or ad hoc terms.
- **Isolation:** Influences from the rest of the world are negligible *or* have
  been absorbed into the variables you keep (for example, static external fields
  you treat as fixed backgrounds are *not* closed unless you also model their
  sources).
- **Boundary in time and space:** You implicitly choose a window where those
  idealizations hold well enough; over longer times, leaks (friction, thermal
  contact, gravity from distant bodies, etc.) usually appear.

## Can closed systems actually exist?

In an everyday, operational sense we approximate them very well (for example,
planets over short spans, particles in accelerator beamlines between
interactions). In a strict, fundamental sense, perfect closure is doubtful:
gravity is long-range, quantum systems entangle with their environments, and any
laboratory apparatus couples to the outside world. The productive move in
theory is to treat “closed” as a *controlled approximation*: enlarge the system
(planet + nearby bodies, system + heat bath model, etc.) until the coupling you
neglected is below the precision you care about.

## Open system

An *open* system exchanges energy, momentum, particles, or (more broadly)
information with an environment you do *not* fully track. Its effective dynamics
then needs extra structure: dissipative forces, noise, driving terms, or
explicit coupling to external fields or reservoirs. Often the honest picture is
that the *compound* “system + environment” is closed, while the subsystem you
focus on is open because you trace out or average over the rest.

## Takeaway for later lectures

Classical mechanics will usually start from closed, deterministic models; when
real devices behave otherwise, we either widen the model or admit open-system
descriptions. Recognizing which idealization you are using is part of using the
theory correctly.
