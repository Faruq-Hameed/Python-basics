# Python Lists

# Lists are used to store multiple items in a single variable(like an array in Js.).

'''
Lists are one of 4 built-in data types in Python used to 
store collections of data, the other 3 are Tuple, Set, 
and Dictionary, all with different qualities and usage.
Lists are created using square brackets:
'''
myList= ['apple', 'orange', 'mango']
print (myList) #['apple', 'orange', 'mango']

# List Items
# List items are ordered, changeable, and allow duplicate values.

# List items are indexed, the first item has index [0], the second item has index [1] etc.

# myList[7] = 'pawpaw'  # ERROR Code
print(myList)

# Ordered

'''When we say that lists are ordered, 
it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

Note: There are some list methods that will change the order, but in general: 
the order of the items will not change.'''

# To determine how many items a list has, use the len() function:
print(myList.__len__()) # i.e print(len(myList)) // 3

print(type(myList))

