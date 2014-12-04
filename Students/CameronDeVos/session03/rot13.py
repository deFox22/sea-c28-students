from __future__ import print_function

# From the link in the task notes and your tip during class
# I found the encoding section of the python site
# to help me easily rot13 some text! Sweetness!
# Reference: https://docs.python.org/2/library/codecs.html
import codecs


def rot13_encrypt(text):
    return codecs.encode(text, "rot-13")


def rot13_longencrypt(text):
    text = text.lower()
    code = ""
    for character in text:
        if character in "abcdefghijklmnopqrstuvwxyz":
            num = ord(character)
            num += 13
            if num > ord("z"):
                num -= 26
            code = code + chr(num)
        else:
            code = code + character
    return code
