#!/usr/bin/env python

import unittest
import cStringIO
import codecs
# importing the html_rendering code with a short name for easy typing.
import html_render as hr


# writing the file out:
def render(page, filename):
    u"""
    render the tree of elements
    This uses cSstringIO to render to memory, then dump to console and
    write to file -- very handy!
    """
    f = cStringIO.StringIO()
    page.render(f)
    f.reset()
    codecs.open(filename, 'w', encoding="utf-8").write(f.read())
    return f.read()
