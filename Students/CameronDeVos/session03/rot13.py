from __future__ import print_function

# From the link in the task notes and your tip during class
# I found the encoding section of the python site
# to help me easily rot13 some text! Sweetness!
# Reference: https://docs.python.org/2/library/codecs.html
import codecs


def rot13_encrypt(text):
    """Take a text statement and return it with a rot-13 cypher"""
    return codecs.encode(text, "rot-13")


def rot13_longencrypt(text):
    """Take in a text statement and return it with a rot-13 cypher"""
    code = ""
    for character in text:
        if character in "abcdefghijklmnopqrstuvwxyz":
            num = ord(character)
            num += 13
            if num > ord("z"):
                num -= 26
            code = code + chr(num)
        elif character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            num = ord(character)
            num += 13
            if num > ord("Z"):
                num -= 26
            code = code + chr(num)
        else:
            code = code + character
    return code

# Test functions for whitespace, punctuation, and capitalization
if __name__ == '__main__':
    assert rot13_encrypt("hello") == "uryyb"
    assert rot13_encrypt("I'm m@king Cookies!") == "V'z z@xvat Pbbxvrf!"
    assert rot13_longencrypt("hello") == "uryyb"
    assert rot13_longencrypt("I'm m@king Cookies!") == "V'z z@xvat Pbbxvrf!"

    print ("All Tests Pass")
