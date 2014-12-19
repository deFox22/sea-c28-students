#!/usr/bin/env python


"""
Simple iterator examples
"""
from __future__ import print_function


class IterateMe_1(object):
    u"""
    About as simple an iterator as you can get:
    returns the sequence of numbers from zero to 4
    ( like xrange(4) )
    """
    def __init__(self, stop=5):
        self.current = -1
        self.stop = stop

    def __iter__(self):
        return self

    def next(self):
        self.current += 1
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


class IterateMe_2(object):
    u"""
    About as simple an iterator as you can get:
    returns the sequence of numbers from zero to 4
    ( like xrange(4) )
    """

    def __init__(self, start=-1, stop=5, step=1):
        self.start = start
        self.current = start - step
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.current = self.start - self.step
        return self

    def next(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration
