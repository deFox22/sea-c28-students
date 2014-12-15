#!/usr/bin/env python


class Element(object):
    u"""A element with content items and optional attributes."""
    tag = u"html"
    indent = u"    "

    def __init__(self, content=None, **kwargs):
        u"""Initialize an Element with content items and optional attributes.

        Keyword arguments:
        content -- content of the Element.
        kwargs -- optional attributes.
        """
        if content:
            self.content = [content]
        else:
            self.content = []
        self.attributes = kwargs
