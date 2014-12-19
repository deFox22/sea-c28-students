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

    def test_html(self):
        u"""Test that html is constructed."""
        page = hr.Html()
        actual = render(page)
        expected = u"<!DOCTYPE html>\n<html>\n</html>"
        self.assertEquals(expected, actual)

    def test_body(self):
        u"""Test that body is constructed."""
        page = hr.Html()
        body = hr.Body()
        page.append(body)
        actual = render(page)
        expected = u"<!DOCTYPE html>\n<html>\n    <body>\n    </body>\n</html>"
        self.assertEquals(expected, actual)

    def test_p(self):
        u"""Test that p is constructed."""
        page = hr.Html()
        p = hr.P()
        page.append(p)
        actual = render(page)
        expected = u"<!DOCTYPE html>\n<html>\n    <p>\n    </p>\n</html>"
        self.assertEquals(expected, actual)

    def test_head(self):
        u"""Test that head is constructed."""
        page = hr.Html()
        head = hr.Head()
        page.append(head)
        actual = render(page)
        expected = u"<!DOCTYPE html>\n<html>\n    <head>\n    </head>\n</html>"
        self.assertEquals(expected, actual)

    def test_Element_attributes(self):
        u"""Test that attributes are assigned to elements."""
        page = hr.Html()
        body = hr.Body(id=u"TheList", style=u"color: red")
        body.append(hr.P(u"Paragraph", style=u"text-align: center;"
                         " font-style: oblique;"))
        page.append(body)
        actual = render(page)
        expected = u"<!DOCTYPE html>\n<html>\n"\
                   "    <body style='color: red' id='TheList'>\n"\
                   "        <p style='text-align: center;"\
                   " font-style: oblique;'>\n            Paragraph\n"\
                   "        </p>\n    </body>\n</html>"
        self.assertEquals(expected, actual)

if __name__ == '__main__':
    unittest.main()
