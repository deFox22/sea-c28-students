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
# Start of user interaction


def main_menu():
    # TODO: Add docstring and ability to quit!
    reply = None
    while reply is None:
        reply = safe_input(u"\nPlease select from the following:\n"
                           "To send a thank you type '1'\nTo "
                           "create a report type '2'\n"
                           "To exit type 'q'\n"
                           "--->  ")
        if reply == 'q':
            print (u"Exiting the script")
        elif reply == '1':
            print (u'Thank You Creation Wizard:')
            thank_you_name()
        elif reply == '2':
            print (u'creating report....')
            create_report()
        else:
            print (u'Sorry that is an invalid answer')
            main_menu()
