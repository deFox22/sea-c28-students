#!/usr/bin/env python
"""code that tests the count_evens function in count_evens.py
can be run with py.test
"""
from count_evens import count_evens


def test_count_evens():
    assert count_evens([-4, -2.2, 0, 3, 4]) == 3
