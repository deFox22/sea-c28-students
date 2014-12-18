#!/usr/bin/env python
u"""code that tests the fibonacci, lucas, and sum_series functions
defined in series.py
Can be run with py.test
"""

from series import fibonacci
from series import lucas
from series import sum_series


fibonacci_series = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5)
    ]

lucas_series = [
    (0, 2),
    (1, 1),
    (2, 3),
    (3, 4),
    (4, 7),
    (5, 11)
    ]


def test_fibonacci():
    u"""Test the fibonacci and sum_series functions with fibonacci series"""
    for n, result in fibonacci_series:
        assert fibonacci(n) == result
        assert sum_series(n) == result


def test_lucas():
    u"""Test the lucas and sum_series functions with lucas series"""
    for n, result in lucas_series:
        assert lucas(n) == result
        assert sum_series(n, 2, 1) == result
