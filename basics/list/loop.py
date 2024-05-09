# Loop Through a List
# # You can loop through the list items by using a for loop:

myList= ['apple', 'orange', 'banana', 'mango']

for ele in myList:
    print ({ele})

# Using a While Loop
# You can loop through the list items by using a while loop.

''''
Use the len() function to determine the length of the list, 
then start at 0 and loop your way through the list items by referring to their indexes.
Remember to increase the index by 1 after each iteration
'''

myList= ['apple', 'orange', 'banana', 'mango']

i=0

while i < len(myList):
    print (myList[i])
    i += 1

''''
Looping Using List Comprehension
List Comprehension offers the shortest syntax for looping through lists:
Example
A short hand for loop that will print all items in a list:
'''

thisList = ["apple", "banana", "cherry"]
[print({'x': x} ) for x in thisList]

'''
List Comprehension
List comprehension offers a shorter syntax when you want to 
create a new list based on the values of an existing list.
Example:
Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
Without list comprehension you will have to write a for statement with a conditional test inside:
'''
thisListB = ["apple", "banana", "cumcub", 'orange", "chorry']
newList=[]

# for fruit in thisListB:
#     if 'a' in fruit:
#         newList.append(fruit)
# print(newList)

for x in thisListB:
  if "a" in x:
    newList.append(x)

print(newList)

# With list comprehension you can do all that with only one line of code:

thisListB = ["apple", "banana", "cumcub", 'orange", "chorry']
newListA=[fruit for fruit in thisListB if 'a' in fruit]
print(newListA)