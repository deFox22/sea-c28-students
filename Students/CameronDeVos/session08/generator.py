#!/usr/bin/env python

from __future__ import print_function
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

if __name__ == '__main__':
    our_prime = prime()
    assert next(our_prime) == 2
    assert next(our_prime) == 3
    assert next(our_prime) == 5
    assert next(our_prime) == 7
    print (u"Generator prime test success")
