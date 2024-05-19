# Python - Copy Lists

newList = ['foo', 'bar', 'baz']
newListA= [x for x in newList]
print(newListA)

newListB = newListA

print(newListB)

if newListB == newListA:
    print(True)
if newListB == newList:
    print(True)
else: print(False)
newListA= [1, 2  , 3, 4, 5]

print(newListB)

listn = [1, 2, 3, 4, 5]
listA = listn
listn=[]
print(listA)

'''
Copy a List
You cannot copy a list simply by typing list2 = list1, because: 
list2 will only be a reference to list1, and changes made in 
list1 will automatically also be made in list2.
Though not proven with what I practiced above
'''
# There are ways to make a copy, one way is to use the built-in List method copy().
listn = [1, 2, 3,]
listD= listn.copy()
print(listD)

# Another way to make a copy is to use the built-in method list().
anotherList= list(listn)
print(anotherList)

'''
Python - Join Lists
Join Two Lists
There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator. and only list should be concatenated
'''
fruits = ['apple', 'banana', 'orange']
grains=['rice', 'beans']
food= fruits + grains
print(food)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:

foods= []

for i in grains:
    fruits.append(i)
print(fruits) # ['apple', 'banana', 'orange', 'rice', 'beans']

# Or you can use the extend() method, where the purpose is to add elements from one list to another list:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1) # ['a', 'b', 'c', 1, 2, 3]

'''
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position; fruits.insert(1,'orange')
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''

names=['faruq', 'akin', 'lala']
listK=names.remove('faruq')
print(listK)




