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

    def append(self, a_string):
        u"""Add addtional content to the Element"""
        self.content.append(a_string)

    def render(self, file_out, indent=u""):
        u"""Render the Element with attibutes."""
        file_out.write(u"\n%s<%s" % (indent, self.tag))
        for key, value in self.attributes.items():
            file_out.write(u" %s='%s'" % (key, value))
        file_out.write(u">")
        for item in self.content:
            try:
                item.render(file_out, indent + self.indent)
            except AttributeError:
                file_out.write(u"\n" + indent + self.indent)
                file_out.write(unicode(item))
        file_out.write(u"\n" + indent)
        file_out.write(u"</%s>" % self.tag)


class Html(Element):
    u"""Element for an HTML tag."""
    tag = u"html"

    # Overwrite the render method to add the '<!DOCTYPE html>'
    def render(self, file_out, indent=u""):
        u"""Render the Element."""
        file_out.write(u"<!DOCTYPE html>")
        # Call superclass render
        Element.render(self, file_out, indent)


class Body(Element):
    u"""Element for a body."""
    tag = u"body"


class P(Element):
    u"""Element for a paragraph."""
    tag = u"p"


class Head(Element):
    u"""Element for a head."""
    tag = u"head"


class OneLineTag(Element):
    u"""Element that renders on one line."""
    # Override the render method to render everything on one line.
    def render(self, file_out, indent=u""):
        u"""Render the Element."""
        file_out.write(u"\n%s<%s" % (indent, self.tag))
        for key, value in self.attributes.items():
            file_out.write(u"%s='%s'" % (key, value))
        file_out.write(u">")
        for item in self.content:
            try:
                item.render(file_out)
            except AttributeError:
                file_out.write(unicode(item))
        file_out.write(u"</%s>" % self.tag)


class Title(OneLineTag):
    u"""Element for a title."""
    tag = u"title"
