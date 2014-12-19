#!/usr/bin/env python

import math


def intsum():
    u"""Generate the sum of the integers in sequence."""
    i = 1
    while True:
        yield sum(range(i))
        i += 1
