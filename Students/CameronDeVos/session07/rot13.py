from __future__ import print_function

# From the link in the task notes and your tip during class
# I found the encoding section of the python site
# to help me easily rot13 some text! Sweetness!
# Reference: https://docs.python.org/2/library/codecs.html
import codecs


def rot13_encrypt(text):
    u"""Take a text statement and return it with a rot-13 cypher"""
    return codecs.encode(text, u"rot-13")
