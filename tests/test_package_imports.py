"""Smoke tests: package layout and imports."""

from theoretical_minimum import __version__
from theoretical_minimum.book1 import lecture_01


def test_version_is_pep440ish() -> None:
    parts = __version__.split(".")
    assert len(parts) >= 2
    assert all(p.isdigit() for p in parts[:2])


def test_lecture_01_package_importable() -> None:
    assert lecture_01.__doc__ is not None
    assert "Lecture 1" in lecture_01.__doc__
