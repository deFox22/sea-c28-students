#!/usr/bin/python

from __future__ import print_function
import codecs
import sys
import string


def overwrite(filename):
    u"""Removes the leading and trailing whitespace on each line from file."""
    f = codecs.open(filename).readlines()
    clean_lines = map(string.strip, f)
    f = codecs.open(filename, 'w')
    for line in clean_lines:
        f.write(line + "\n")
    f.close()
