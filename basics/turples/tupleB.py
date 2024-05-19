'''
Unpacking a Tuple
When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
'''
# Packing a tuple:
fruits = ("apple", "banana", "cherry")

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
# Note: The number of variables must match the number of values in the tuple, 
# if not, you must use an asterisk to collect the remaining values as a list.
(black, *grey) = fruits
print(grey) # ['banana', 'cherry']

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits
print(tropic) # [ 'mango', 'papaya', 'pineapple]

'''Loop Through a Tuple
You can loop through the tuple items by using a for loop.
Loop Through the Index Numbers
You can also loop through the tuple items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.
To join two or more tuples you can use the + operator:


'''

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

'''Multiply Tuples
If you want to multiply the content of a tuple a given number of times, you can use the * operator:
'''
tuple4= tuple3 * 2
print(tuple4) # ('a', 'b', 'c', 1, 2, 3, 'a', 'b', 'c', 1, 2, 3)