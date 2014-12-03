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
