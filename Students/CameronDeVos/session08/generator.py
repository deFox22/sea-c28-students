#!/usr/bin/env python

import math


def intsum():
    u"""Generate the sum of the integers in sequence."""
    i = 1
    while True:
        yield sum(range(i))
        i += 1


def doubler():
    u"""Generate the double of the previous value."""
    value = 1
    while True:
        yield value
        value *= 2
