#!/usr/bin/python

from __future__ import print_function


def safe_input(prompt):
    try:
        response = raw_input(prompt)
    except (EOFError, KeyboardInterrupt):
        print (u"Sorry, unable to preform that action")
        return safe_input(prompt)
    else:
        return unicode(response)
