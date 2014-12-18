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

class Test_html_render(unittest.TestCase):
    u""" Unittest Class to test the html_render file."""
    def test_step8(self):
        u"""Test that the output of step8 instructions matches expected."""
        page = hr.Html()
        head = hr.Head()
        head.append(hr.Meta(charset=u"UTF-8"))
        head.append(hr.Title(u"PythonClass = Revision 1087:"))
        page.append(head)
        body = hr.Body()
        body.append(hr.H(2, u"PythonClass - Class 6 example"))
        body.append(hr.P(u"Here is a paragraph of text -- there could be more"
                         " of them, but this is enough to show"
                         " that we can do some text",
                         style=u"text-align: center; font-style: oblique;"))
        body.append(hr.Hr())
        list = hr.Ul(id=u"TheList", style=u"line-height:200%")
        list.append(hr.Li(u"The first item in a list"))
        list.append(hr.Li(u"This is the second item", style="color: red"))
        item = hr.Li()
        item.append(u"And this is a ")
        item.append(hr.A(u"http://google.com", "link"))
        item.append(u"to google")
        list.append(item)
        body.append(list)
        page.append(body)
        render(page, u"test_html_output8.html")
        with open("test_html_output8.html", "r") as myfile:
            actual = myfile.readlines()
        with open("expected_test_html_output8.html", "r") as exfile:
            expected = exfile.readlines()
        self.assertEquals(expected, actual)

if __name__ == '__main__':
    unittest.main()
