#!/usr/bin/python

from __future__ import print_function


def safe_input(prompt):
    try:
        response = raw_input(prompt)
    except (EOFError, KeyboardInterrupt):
        print (u"Sorry, unable to preform that action")
        return safe_input(prompt)
    else:
        return unicode(response)


def float_check(amount):
    try:
        float(amount)
        return True
    except ValueError:
        return False


# Create donor database
donorbase = {u"Tony Tiger": [88.00, 22.19],
             u"Melody Mandy": [23.00]}


def print_names(database):
    print (u"Donors:\n")
    for key in database:
        print (key)
    print (u"\n")


def add_donor(name, amount=0):
    donorbase[name] = [amount]


def update_donor(name, amount):
    donorbase[name].append(amount)
