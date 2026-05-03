"""Tests for Lecture 2, Exercise 8 — four parametric plane motions."""

from __future__ import annotations

import math

import pytest

from theoretical_minimum.book1.lecture_02 import exercise_08


def test_cos_exp_at_origin() -> None:
    k = exercise_08.kinematic_cos_exp(omega=1.0, t=0.0)
    assert k.position == pytest.approx((1.0, 1.0))
    assert k.velocity == pytest.approx((0.0, 1.0))
    assert k.speed == pytest.approx(1.0)
    assert k.acceleration == pytest.approx((-1.0, 1.0))


def test_phased_circle_constant_speed() -> None:
    for t in (0.0, 0.3, -1.1, math.pi / 5):
        k = exercise_08.kinematic_phased_circle(omega=2.5, phi=0.4, t=t)
        assert k.speed == pytest.approx(abs(2.5))
        rx, ry = k.position
        ax, ay = k.acceleration
        assert ax == pytest.approx(-(2.5**2) * rx)
        assert ay == pytest.approx(-(2.5**2) * ry)


def test_astroid_speed_closed_form() -> None:
    c, t = -1.25, 0.37
    k = exercise_08.kinematic_astroid(c=c, t=t)
    vx, vy = k.velocity
    assert math.hypot(vx, vy) == pytest.approx(k.speed)
    assert k.speed == pytest.approx(1.5 * abs(c) * abs(math.sin(2.0 * t)))


def test_astroid_acceleration_matches_finite_difference() -> None:
    c, t = 2.0, 0.55
    k = exercise_08.kinematic_astroid(c=c, t=t)
    h = 1e-7
    k_plus = exercise_08.kinematic_astroid(c=c, t=t + h)
    k_minus = exercise_08.kinematic_astroid(c=c, t=t - h)
    num_ax = (k_plus.velocity[0] - k_minus.velocity[0]) / (2 * h)
    num_ay = (k_plus.velocity[1] - k_minus.velocity[1]) / (2 * h)
    assert k.acceleration[0] == pytest.approx(num_ax, rel=1e-5, abs=1e-5)
    assert k.acceleration[1] == pytest.approx(num_ay, rel=1e-5, abs=1e-5)


def test_cycloid_speed_closed_form() -> None:
    c, t = 3.0, 1.1
    k = exercise_08.kinematic_cycloid(c=c, t=t)
    vx, vy = k.velocity
    assert math.hypot(vx, vy) == pytest.approx(k.speed)
    assert k.speed == pytest.approx(2.0 * abs(c) * abs(math.sin(0.5 * t)))


def test_cycloid_acceleration() -> None:
    c, t = -0.7, 2.3
    k = exercise_08.kinematic_cycloid(c=c, t=t)
    assert k.acceleration == pytest.approx((c * math.sin(t), c * math.cos(t)))
