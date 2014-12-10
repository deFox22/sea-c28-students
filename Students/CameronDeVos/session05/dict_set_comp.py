#!/usr/bin/python

from __future__ import print_function

food_pref = {u"name": u"Cameron",
             u"city": u"Seattle",
             u"cake": u"chocolate",
             u"fruit": u"mangos",
             u"salad": u"caesar",
             u"pasta": u"macaroni"}

# Print the dictionary by passing it to a string format method
print (u"{name} is from {city}, and he likes {cake} cake, {fruit} fruit, "
       "{salad} salad, and {pasta} pasta.\n".format(**food_pref))

# Use list comprehension to build a dictionary of numbers from 0 to 15 and the
# hexidecimal equivalent
hexidict1 = dict(zip(range(16), [hex(x) for x in range(16)]))
print (u"hexidict1 {0}\n".format(hexidict1))

# Do the previous entirely whith a dict comprehension
hexidict2 = {i: hex(i) for i in range(16)}
print (u"hexidict2 {0}\n".format(hexidict2))

# Using the food_pref dictioanry: Make a dictionary using the same keys
# but with the number of a's in each value
number_a = food_pref.copy()
number_a = {key: value.count(u"a") for key, value in number_a.iteritems()}
print (u"number_a: {0}\n".format(number_a))
