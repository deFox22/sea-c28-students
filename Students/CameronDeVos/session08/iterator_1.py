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

if __name__ == "__main__":
    print (u"first version")
    for i in IterateMe_1():
        print (i)

    print (u"second version")
    it = IterateMe_2(2, 20, 2)
    for i in it:
        if i > 10:
            break
        print (i)
    for i in it:
        print (i)

    print(u"xrange version")
    itx = xrange(2, 20, 2)
    for x in itx:
        if x > 10:
            break
        print (x)
    for x in itx:
        print(x)
