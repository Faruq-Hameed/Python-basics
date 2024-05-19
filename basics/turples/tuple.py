'''
Tuple
Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data,
the other 3 are List, Set, and Dictionary, all with different qualities and usage.
A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
Tuple items are ordered, unchangeable, and allow duplicate values.
Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
Since tuples are indexed, they can have items with the same value:
A tuple can contain different data types:

From Python's perspective, tuples are defined as objects with the data type 'tuple':

<class 'tuple'>
'''

tuple_a = ('a', 'b', 'c', 'd', 'e')
print(tuple_a)
# tuple_a[0] ='a' # ERROR; 'tuple' object does not support item assignment
fruit_items= ('apple', 'orange', 'mango')

# To determine how many items a tuple has, use the len() function:
print(len(fruit_items)) # 3

'''To create a tuple with only one item, you have to add a comma after the item, 
otherwise Python will not recognize it as a tuple.'''
fruits=('cashew') 

print(type(fruits)) # <class 'str'>

fruits_a=('cashew',)
print(type(fruits_a)) # <class 'tuple'>

# It is also possible to use the tuple() constructor to make a tuple.

items= tuple(('apple','banana')) # note the double round-brackets
print(items)

'''
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When choosing a collection type, it is useful to understand the properties of that type. 
Choosing the right type for a particular data set could mean retention of meaning, 
and, it could mean an increase in efficiency or security.
'''

# You can access tuple items by referring to the index number, inside square brackets:
tuple_mems=tuple(['a', 'b', 'c'])
print(type(tuple_mems))
print(tuple_mems[0])

