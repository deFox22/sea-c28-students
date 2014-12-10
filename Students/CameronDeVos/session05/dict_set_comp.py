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
