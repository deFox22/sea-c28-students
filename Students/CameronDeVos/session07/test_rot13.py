#!/usr/bin/env python
u"""Code that tests the encrypt function defined in rot13.py
Can be run with py.test
"""

from rot13 import rot13_encrypt


def test_phrase():
    assert rot13_encrypt(u"I'm m@king Cookies!") == u"V'z z@xvat Pbbxvrf!"
