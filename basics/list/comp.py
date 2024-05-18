# List Comprehension

# List comprehension offers a shorter syntax when you want 
# to create a new list based on the values of an existing list.

fruits = ['apple','mond', 'orange', 'banana', 'pod']
newList=[]

# Without list comprehension
for fruit in fruits:
    if 'a' in fruit:
        newList.append(fruit)
print(newList) #['apple', 'orange', 'banana', 'mango']

# With list comprehension you can do all that with only one line of code:

# The Syntax
# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.
# The condition is like a filter that only accepts the items that valuate to True.

newListB = [fruit for fruit in fruits if 'a' in fruit]
print(newListB)

# Only accept items that are not "apple":
newListC= [fruit for fruit in fruits if  fruit != 'apple']
print(newListC) # ['mond', 'orange', 'banana', 'pod']
'''
The condition if x != "apple"  will return True for all 
elements other than "apple", making the new list contain all fruits except "apple".
The condition is optional and can be omitted:
'''
newListD = [x for x in fruits]

print(newListD) # ['apple', 'mond', 'orange', 'banana', 'pod']

# Iterable
# The iterable can be any iterable object, like a list, tuple, set etc.
newListF = [x for x in range(10)]
print(newListF) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
newListF = [x for x in range(10) if x <= 6]
print(newListF) #[0, 1, 2, 3, 4, 5, 6]

"""Expression
The expression is the current item in the iteration, but it is also the outcome, 
which you can manipulate before it ends up like a list item in the new list:"""

newListG = [x.upper() for x in fruits]
print(newListG)

# Python - Sort Lists
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

num= [8,9,0,3,8,3,83,8,93,3]
num.sort()
print(num) # [0, 3, 3, 3, 8, 8, 8, 9, 83, 93]

# Sort Descending
# To sort descending, use the keyword argument reverse = True:
thislist.sort(reverse=True)
print(thislist) # ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

num.sort(reverse=True)
print(num) # [93, 83, 9, 8, 8, 8, 3, 3, 3, 0]

# By default the sort() method is case sensitive, 
# resulting in all capital letters being sorted before lower case letters

'''You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first):

Example
Sort the list based on how close the number is to 50:'''

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 20]
thislist.sort(key = myfunc)
print(thislist) # [50, 65, 23, 82, 100]

# Case sensitive sorting can give an unexpected result:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) # ['Kiwi', 'Orange', 'banana', 'cherry']
'''
Luckily we can use built-in functions as key functions when sorting a list.

So if you want a case-insensitive sort function, use str.lower as a key function:

Example
Perform a case-insensitive sort of the list:'''

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) # ['banana', 'cherry', 'Kiwi', 'Orange']

# Reverse Order
# What if you want to reverse the order of a list, regardless of the alphabet?

# The reverse() method reverses the current sorting order of the elements.
thislist.reverse()
print(thislist) # ['banana', 'orange