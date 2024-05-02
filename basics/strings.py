''''
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
'''
# Example
# Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[0]) # H
print(a[1]) # e

# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.

for ele in a:
    print(ele) 
    if ele == 'e':
        print('element is e ==', ele)


# To get the length of a string, use the len() function.
print(len(a)) # 13

# To check if a certain phrase or character is present in a string, we can use the keyword in.

print ('e' in a) # true
print ('el' in a) # true
print ('elc' in a) # false

txt = "The best things in life are free!"

if ('best' in txt):
    print('txt contains "best"')
    
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

print('hal' not in a) # true

if 'freed' not in txt:
    print('freed is not there')

'''
Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.
the specified end index is not returned
'''

ltt= 'world'
print('letter is ', ltt[0:3]) #letter is  wor

# By leaving out the start index, the range will start at the first character
# By leaving out the end index, the range will go to the end

print('letter is ', ltt[:4]) #letter is  worl

# Use negative indexes to start the slice from the end of the string:
# negative index start from -1 i.e last index is -1
print('letter is ', ltt[-3:-1]) #letter is  rl
