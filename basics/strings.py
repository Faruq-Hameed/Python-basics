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