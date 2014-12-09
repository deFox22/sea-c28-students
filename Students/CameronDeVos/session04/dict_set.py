# session04 - Dictionaries and Sets
from __future__ import print_function

# Section 1
# Create a dictionary with Chris from Seattle who likes Chocolate
dictionary1 = {u'name': u'Chris', u'city': u'Seattle', u'cake': u'Chocolate'}
# Display dictionary
print (dictionary1)
# Delete the entry for Cake
del dictionary1[u'cake']
# Display dictionary
print (dictionary1)
# Add an entry for fruit with mango and display dictionary
dictionary1[u'fruit'] = u'Mango'
print (dictionary1)
# Display the dictionary keys
print (dictionary1.keys())
# Display the dictionary values
print (dictionary1.values())
# Display whether or not "cake" is a key in the dictionary
print (u'cake' in dictionary1)
# Display whether or not "Mango" is a value in the dictionary
print (u'Mango' in dictionary1.values())

# Section 2
# Use dict constructor and zip to build a dictionary of numbers
# from 0 to 15 and the hexadecimal equivalent
nums = (range(16))
hexs = (u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7',
        u'8', u'9', u'a', u'b', u'c', u'd', u'e', u'f', u'g')
newdict = dict(zip(nums, hexs))
print (newdict)

# Section 3
# Use the dict from section 1 to make a dict
# using the same keys but with the # of a's in each value
# TODO Shorten
dictionary2 = {}
for key, value in dictionary1.items():
    count = 0
    for letter in value:
        if letter == u'a':
            count += 1
    dictionary2[key] = count
print (dictionary2)

# Section 4
# Create sets s2, s3, and s4 that contain numbers
# from zero to 20, divisible 2,3, and 4


def divisible_set(nums, divisor):
    alist = []
    for num in range(nums):
        if num % divisor == 0:
            alist.append(num)
    return set(alist)

s2 = divisible_set(21, 2)
s3 = divisible_set(21, 3)
s4 = divisible_set(21, 4)
# Display the sets
print (s2)
print (s3)
print (s4)
# Display if s3 is a subset of s2
print (s3.issubset(s2))
# Display if s4 is a subset of s2
print (s4.issubset(s2))

# Section 5
# Create a set with the letters in 'Python' and add 'i' to the set
spy = set([u'P', u'y', u't', u'h', u'o', u'n'])
spy.add(u'i')
# Create a frozenset with the letters in 'marathon'
fs = frozenset((u'm', u'a', u'r', u'a', u't', u'h', u'o', u'n'))
# display the union and intersection of the two sets
print (spy.union(fs))
print (spy.intersection(fs))
