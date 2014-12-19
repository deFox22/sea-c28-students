#!usr/bin/env python

import sys
import time


class Timer(object):
    u"""Returns the elapsed run time."""
    def __init__(self, output=sys.stdout):
        super(Timer, self).__init__()
        self.output = output

    def __enter__(self):
        self.start = time.time()
        return self.start

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time() - self.start
        result = u"this code took {:.6f} seconds".format(end_time)
        self.output.write(result)

if __name__ == '__main__':
    with Timer() as t:
        for i in range(100000):
            i = i ** 20
