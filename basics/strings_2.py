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



### General PRD for Point-Based System

print(b.replace('!', ' from me'))# Hello, World from me
print(len(b.replace('!', ' from me')))# checking length of string //22

# The split() method returns a list where the text between the specified separator becomes the list items.

print(b.split(',')) #[' Hello', ' World! ']
print(b.split('l')) # [' He', '', 'o, Wor', 'd! ']

# To concatenate, or combine, two strings you can use the + operator.

print(a + b) # Hello, World! Hello, World!

print('book' + ' warm.') # book warm.

c = 'Faruq'

d= b + c+ " " + 'hameed'

print({d}) # {' Hello, World! Faruq'}

# we cannot combine strings and numbers

age = 36
# txt = "My name is John, I am " + age
# print(txt) #ERROR: can only concatenate str (not "int") to str

#  we can combine strings and numbers by using f-strings or the format() method!

"""
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal,
and add curly brackets {} as placeholders for variables and other operations. """


# aged=20
# txtA= f'Hello{aged}'
# print(txtA) #ERROR: can only concatenate

age = 36
txt = format("My name is John,77 I am {age}") #My name is John,77 I am {age}
print(txt)

txt = f"My name is am {age}" #My name is am 36
print(txt)
