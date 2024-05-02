# Modify Strings

# Python has a set of built-in methods that you can use on strings.

a = "Hello, World!"
print(a.upper()) # HELLO, WORLD! //Return a copy of the string converted to uppercase
print(a.lower()) # hello, world!
print(a.find('o')) # 4
print(a.endswith('!')) # True
print(a.isalnum()) # False //Return True if the string is an alpha-numeric string, False otherwise.

#The strip() method removes any whitespace from the beginning or the end:

b = " Hello, World! "

print(b.strip()) #Hello, World!

# The replace() method replaces a string with another string:

print(b.replace('!', ' from me'))# Hello, World from me
print(len(b.replace('!', ' from me')))# checking length of string //22

# The split() method returns a list where the text between the specified separator becomes the list items.

print(b.split(',')) #[' Hello', ' World! ']
print(b.split('l')) # [' He', '', 'o, Wor', 'd! ']
