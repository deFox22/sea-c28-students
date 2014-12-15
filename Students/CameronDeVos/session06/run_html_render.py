#!/usr/bin/env python

"""
a simple script can run and test your html rendering classes.
Uncomment the steps as you add to your rendering.
"""
import codecs
import cStringIO


# importing the html_rendering code with a short name for easy typing.
import html_render as hr

## writing the file out:


def render(page, filename):
    """
    render the tree of elements
    This uses cSstringIO to renderto memory, then dump to console and
    write to file -- very handy!
    """

    f = cStringIO.StringIO()
    page.render(f)

    f.reset()

    print f.read()

    f.reset()
    codecs.open(filename, 'w', encoding="utf-8").write( f.read() )


## Step 1
##########

page = hr.Element()

page.append(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text")

page.append(u"And here is another piece of text -- you should be able to add any number")

render(page, u"test_html_output1.html")