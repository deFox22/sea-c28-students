from __future__ import print_function


def count_evens(nums):
    """Takes in a list of numbers and returns the number of evens in list"""
    return len([num for num in nums if num % 2 == 0])

if __name__ == '__main__':
    assert count_evens([2, 1, 2, 3, 4]) == 3
    assert count_evens([1, 3, 5]) == 0
    print (u"All Tests Pass")
