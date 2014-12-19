#!/usr/bin/env python

import unittest
import cStringIO
# importing the html_rendering code with a short name for easy typing.
import html_render as hr


# writing the file out:
def render(page):
    u"""
    render the tree of elements
    This uses cSstringIO to render to memory, then dump to console and
    write to file -- very handy!
    """
    f = cStringIO.StringIO()
    page.render(f)
    f.reset()
    return f.read()


class Test_html_render(unittest.TestCase):
    u"""Unittest Class to test the html_render file."""

    def test_element_tag(self):
        u"""Test that tag is correctly constructed"""
        page = hr.Element(u"TagsTagsTags")
        actual = render(page)
        expected = u"\n<html>\n    TagsTagsTags\n</html>"
        self.assertEquals(expected, actual)

    def test_append(self):
        u"""Test that strings are append to element."""
        page = hr.Element(u"String One")
        page.append(u"String Two")
        actual = render(page)
        expected = u"\n<html>\n    String One\n    String Two\n</html>"
        self.assertEquals(expected, actual)

if __name__ == '__main__':
    unittest.main()
