#!/usr/bin/env python

from __future__ import print_function

# Section 1
# Create a list that contains "Apples", "Pears", "Oranges", and "Peaches".
fruits1 = [u"Apples", u"Pears", u"Oranges", u"Peaches"]
# Display the list
print(fruits1)
# Ask the user for another fruit and add it to the end of the list.
while True:
    user_fruit = unicode(raw_input(u"Add a fruit type "
                                   "not already in the list. -> "))
    if user_fruit.title() not in fruits1:
        fruits1.append(user_fruit.title())
        break
    else:
        print(u"That fruit is already in the list. Pick again.")
# Display the list
print (fruits1)
# Ask the user for a number and display the number back to the user and
# the fruit corresponding to that number (on a 1-is-first basis).
while True:
    user_number = int(raw_input(u"Pick a number between 1 "
                                "and %s. ->" % len(fruits1)))
    if user_number <= len(fruits1) and user_number >= 1:
        print (u"The fruit at spot %s "
               "is %s." % (user_number, fruits1[(user_number)-1]))
        break
    else:
        print (u"That is an invalid answer. Pick again.")
# Add another fruit to the beginning of the list using "+" and display list.
fruits1 = [u"Plums"] + fruits1
print (fruits1)
# Add another fruit to the beginning of the list using insert and display list.
fruits1.insert(0, u"Mangos")
print (fruits1)
# Display all the fruits that begin with "P", using a for loop.
for fruit in fruits1:
    if fruit[0] == "P":
        print (fruit)
