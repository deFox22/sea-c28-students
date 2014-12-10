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
