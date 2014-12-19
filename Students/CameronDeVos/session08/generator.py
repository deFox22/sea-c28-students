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


def fib():
    u"""Generate the fibonacci series."""
    previous = 0
    current = 1
    while True:
        yield current
        previous, current = current, current + previous


def prime():
    u"""Generate the prime numbers."""
    number = 2
    while True:
        if prime_check(number):
            yield number
        number += 1


def prime_check(number):
    u"""Take in a number and check if it is a prime number."""
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for num in range(3, int(math.sqrt(number)+1), 2):
            if number % num == 0:
                return False
        return True
    return False
