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
