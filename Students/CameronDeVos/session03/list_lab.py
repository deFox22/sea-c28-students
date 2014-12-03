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

# Section 2
fruits2 = fruits1[:]
# Display the list
print (fruits2)
# Remove the last fruit from the list
fruits2.remove(fruits2[-1])
# Display the list
print (fruits2)
# Ask the user for a fruit to delete and find it and delete it.
# Bonus multiply list times 2. Keep asking until a match is found.
# Once found, delete all occurances.
fruits2 = fruits2 * 2
while True:
    user_fruit_delete = unicode(raw_input(u"Which fruit type would "
                                          "you like to delete? -> "))
    if user_fruit_delete.title() in fruits2:
        for fruit in fruits2:
            if fruit == user_fruit_delete.title():
                fruits2.remove(fruit)
        break
    else:
        print (u"That fruit is not in the list. Pick again.")

# Section 3
fruits3 = fruits1[:]
# Ask the user for input displaying a line like "Do you like Apples?".
# For each fruit(make all lowercase). Each "no", delete that fruit
# For any answer other than "yes" or "no", prompt user again
for fruit in fruits3[:]:
    while True:
        user_likes = raw_input(u"Do you like %s? "
                               "yes or no -> " % fruit.lower())
        if user_likes == "no":
            fruits3.remove(fruit)
            break
        elif user_likes != "yes":
            print (u"Please answer with yes or no. Try again.")
        else:
            break
# Display the list
print (fruits3)

# Section 4
# Make a copy of the list and reverse the letters in each fruit in the copy.
fruits4 = fruits1[:]
for spot, fruit in enumerate(fruits1[:]):
    fruits4[spot] = fruit[::-1]
# Delete the last item of original list. Display the original list and copy.
fruits1.remove(fruits1[-1])
print (fruits1)
print (fruits4)
