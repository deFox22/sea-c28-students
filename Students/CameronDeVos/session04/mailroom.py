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

def thank_you_name():
    name = None
    while name is None:
        name = safe_input(u"What is the full name of the donor?\nTo see "
                          "a list of previous donors type 'list'"
                          "To quit the task type 'q'"
                          "\n--->  ")
        if name == u"list":
            print_names(donorbase)
            thank_you_name()
        elif name in donorbase.keys():
            print (u"%s has been found in the donorbase" % name)
            thank_you_amount(name)
        elif name == u"q":
            print (u"returning to main menu")
            main_menu()
        else:
            print (u"%s has been added to the donorbase" % name)
            add_donor(name)
            thank_you_amount(name)


def thank_you_amount(name):
    amount = None
    while amount is None:
        amount = safe_input(u"To return to the main menu type 'q'"
                            "What is the donation amount?\n--->  ")
        if amount == u"q":
            main_menu()
        elif float_check(amount) is False or amount.startswith('-'):
            print (u"Please enter a valid or positive number")
            thank_you_amount(name)
        else:
            amount = round(float(amount), 2)
            print ("made it here")
            print (amount)
            update_donor(name, amount)
            print (donorbase)
            compose_email(name, amount)


def compose_email(name, amount):
    print (u"Thank you for your donation, %s, in\n"
           " the amount of %.2f" % (name, amount))
    main_menu()


def create_report():
    donor_data = []
    for i, name in enumerate(donorbase):
        donor_data.append([name])
        total_donated = round(sum(donorbase[name]), 2)
        donor_data[i].append(total_donated)
        donation_count = len(donorbase[name])
        donor_data[i].append(donation_count)
        average_donation = round((total_donated/donation_count), 2)
        donor_data[i].append(average_donation)
    donor_data.sort(key=lambda x: x[1], reverse=True)
    print ("\n{:<16} {:<12} {:<12} "
           "{:<12}".format("Name", "Total", "Donations", "Average"))
    for name in donor_data:
        print ("{:<16} {:<12} {:<12} "
               "{:<12}".format(name[0], "{:.2f}".format(name[1]), name[2],
                               "{:.2f}".format(name[3])))
    main_menu()

if __name__ == "__main__":
    main_menu()
