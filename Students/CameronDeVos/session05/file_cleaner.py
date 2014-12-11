#!/usr/bin/python

from __future__ import print_function
import codecs
import sys
import string


def overwrite(filename):
    u"""Removes the leading and trailing whitespace on each line from file."""
    f = codecs.open(filename).readlines()
    clean_lines = map(string.strip, f)
    f = codecs.open(filename, 'w')
    for line in clean_lines:
        f.write(line + "\n")
    f.close()


def overwrite_comp(filename):
    u"""Removes the leading and trailing whitespace on each line from file."""
    f = codecs.open(filename).readlines()
    clean_lines = [line.strip() + "\n" for line in f]
    f = codecs.open(filename, 'w').writelines(clean_lines)


def rewrite(filename):
    u"""Reads input file and creates new file with whitespace removed"""
    f = codecs.open(filename).readlines()
    clean_lines = map(string.strip, f)
    f = codecs.open("clean_%s" % filename, 'w')
    for line in clean_lines:
        f.write(line + "\n")
    f.close()


def rewrite_comp(filename):
    u"""Reads input file and creates new file with whitespace removed"""
    f = codecs.open(filename).readlines()
    clean_lines = [line.strip() + "\n" for line in f]
    f = codecs.open("clean_comp_%s" % filename, 'w').writelines(clean_lines)f


if __name__ == '__main__':
    while True:
        try:
            filename = sys.argv[1]
        except IndexError:
            print ("Please provide a file to be cleaned when calling script.")
            break
        filename = sys.argv[1]
        choice = raw_input(u"\nTo clean the inputted file type '1'\n"
                           "To copy the contents and create a clean_comp_%s "
                           "file type '2'\n"
                           "--->  " % filename)
        if choice == "1":
            overwrite_comp(filename)
            print (u"File has been cleaned")
            break
        elif choice == "2":
            rewrite_comp(filename)
            print (u"Copied the file and created"
                   " a new file with clean contents.")
            break
        else:
            print (u"Sorry, that is an invalid response.\n"
                   "Please pick option '1' or '2'.")
