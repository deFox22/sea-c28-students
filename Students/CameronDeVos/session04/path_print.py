#!/usr/bin/python

import os


def path_print():
    """Return files in current directory"""
    files = []
    for f in os.listdir(os.curdir):
        if os.path.isfile(f):
            files.append(f)
    for f in files:
        print f

if __name__ == '__main__':
    path_print()
