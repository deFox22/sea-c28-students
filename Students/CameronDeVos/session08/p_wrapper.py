#!/usr/bin/env python

from __future__ import print_function


def p_wrapper(func):
    u"""Wrap a string in a HTML 'p' tag."""
    def wrap(*args, **kwargs):
        return u"<p> {} </p>".format(func(*args, **kwargs))
    return wrap

if __name__ == '__main__':
    @p_wrapper
    def return_a_string(string):
        return string
    assert return_a_string(u"Wrap") == u"<p> Wrap </p>"
