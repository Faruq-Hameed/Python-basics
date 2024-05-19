'''
Change Tuple Values
Once a tuple is created, you cannot change its values. 
Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list,
 and convert the list back into a tuple
'''

fruits=('a','b','c','d','e','f','g','h')
print(type(fruits)) # <class 'tuple'>

fruitB = fruits
print(type(fruitB)) # <class 'tuple

fruitC = list(fruits)
print(type(fruitC)) # <class 'list'>
print((fruitC)) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

fruits=('a','b')
print(fruits) # ('a', 'b')

#changing the items in the tuples;

fruitD = list(fruits)
fruitD[1] = 'banana'

fruits= tuple(fruitD)
print(fruits) # ('a', 'banana')

# Since tuples are immutable, they do not have a built-in append() method, 
# but there are other ways to add items to a tuple.


# Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), 
# create a new tuple with the item(s), and add it to the existing tuple:

y= ('cashew',)
fruits += y
print(fruits) # ('a', 'banana', 'cashew')

'''
Note: You cannot remove items in a tuple.
Tuples are unchangeable, so you cannot remove items from it, 
but you can use the same workaround as we used for changing and adding tuple items:
'''

# Or you can delete the tuple completely:

# Example
# The del keyword can delete the tuple completely:
del fruits
# print(fruits) # NameError: name 'fruits' is not defined. Did you mean: 'fruitB'?

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists