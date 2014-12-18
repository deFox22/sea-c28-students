from __future__ import print_function


def count_evens(nums):
    u"""Takes in a list of numbers and returns the number of evens in list"""
    return len([num for num in nums if num % 2 == 0])
