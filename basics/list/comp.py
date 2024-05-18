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