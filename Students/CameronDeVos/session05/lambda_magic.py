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


if __name__ == '__main__':
    the_list = function_builder(4)
    assert the_list[0](2) == 2
    assert the_list[1](2) == 3
    print (u"All Tests Pass")
