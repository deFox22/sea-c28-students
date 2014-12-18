from __future__ import print_function


def fibonacci(n):
    u"""Return the nth value of the Fibonacci series."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    u"""Return the nth value of the Lucas series."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, x=0, y=1):
    u"""Return the nth value in a series based on its first two values.

    Keyword arguments:
    n -- the spot in series
    x -- the 1st number in series, default aligned with fibonacci series
    y -- the 2nd number in series, default aligned with fibonacci series
    """
    if n == 0:
        return x
    elif n == 1:
        return y
    else:
        return sum_series(n - 1, x, y) + sum_series(n - 2, x, y)
