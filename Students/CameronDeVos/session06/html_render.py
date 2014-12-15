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


class SelfClosingTag(Element):
    u"""Element with a single tag and attributes, if any."""
    def __init__(self, **kwargs):
        self.attributes = kwargs

    # Override the render method to render just the one tag and attributes.
    def render(self, file_out, indent=u""):
        u"""Render the Element"""
        file_out.write(u"\n%s<%s" % (indent, self.tag))
        for key, value in self.attributes.items():
            file_out.write(u"%s='%s'" % (key, value))
        file_out.write(u"/>")


class Hr(SelfClosingTag):
    u"""Self closing tag for a horizontal rule."""
    tag = u"hr"


class LineBreak(SelfClosingTag):
    u""""Self closing tag for a line break."""
    tag = u"br"


class A(OneLineTag):
    u"""One line tag for an anchor (link)."""
    tag = u"a "

    def __init__(self, link, content):
        OneLineTag.__init__(self, content, href=link)


class Ul(Element):
    u"""Element for an unordered list."""
    tag = u"ul"


class Li(Element):
    u"""Element for the item in a list."""
    tag = u"li"


class H(OneLineTag):
    u"""One line tag for a header."""
    def __init__(self, level, content, **kwargs):
        OneLineTag.__init__(self, content, **kwargs)
        self.tag = u"h%i" % level


class Meta(SelfClosingTag):
    u"""Self closing tag to add the meta to give your document an encoding."""
    tag = u"meta"
