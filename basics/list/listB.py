# Range of Indexes
# Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", {'kk'},"orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # ['cherry', 'orange', 'kiwi']
# Note: The search will start at index 2 (included) and end at index 5 (not included).

# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:

if 'apple' in thislist:
    print("Yes, 'apple' is in the fruits list") # Yes, 'apple' is in the fruits list

# If you insert more items than you replace, the new items will be inserted where you specified, 
# and the remaining items will move accordingly:

thislist[1:3] = ["black","currant", "water","ppp","melon", "apple"]
print(thislist)

""""
Note: The length of the list will change 
when the number of items inserted does not match the number of items replaced.
"""
thislist[1:5] = ["egg"]
print(thislist)

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# The insert() method inserts an item at the specified index:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) # ['apple', 'banana', 'watermelon', 'cherry']

# To add an item to the end of the list, use the append() method:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) # ['apple', 'banana', 'cherry', 'orange']

# To append elements from another list to the current list, use the extend() method.
ListB=['car', 'bike']
thislist.extend(ListB)
print(thislist) # ['apple', 'banana', 'cherry', 'orange', 'car', 'bike']

# The extend() method does not have to append lists, 
# you can add any iterable object (tuples, sets, dictionaries etc.).

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) # ['apple', 'banana', 'cherry', 'kiwi', 'orange']

# The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#removing an unexisting item will throw an exception

# If there are more than one item with the specified value, 
# the remove() method removes the first occurance

# The pop() method removes the specified index or last item if no index is specified
listB = ['a', 'b', 'c', 'd', 'e', 'f']
listB.pop() # ['a', 'b', 'c', 'd', 'e']
print(listB)

listB.pop(2) # ['a', 'b', 'd', 'e']
print(listB)
listB.pop(-2) 
print(listB)# ['a', 'b', 'e']
# The clear() method empties the list: it removes all items from the list and returns t

# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist # Delete the entire list:
# print(thislist) # Error: 'thislist' is not defined

# The clear() method empties the list.

# The list still remains, but it has no content.

# Example
# Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # [] instead of throwing an exception like del




