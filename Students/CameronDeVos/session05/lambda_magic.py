#!/usr/bin/python
from __future__ import print_function

# Write a function that returns a list of n functions, such that each one,
# when called, will return the input value, incremented
# by an increasing number

# Extra credit: Do it with a list comprehension, instead of a for loop


def function_builder(n):
    u"""Return a list of n functions.

    The n functions return the input value, incremented by increasing number
    """
    func_list = [lambda x, y=i: x+y for i in range(n)]
    return func_list
