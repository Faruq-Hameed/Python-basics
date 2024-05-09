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

# Placeholders and Modifiers: A placeholder can contain variables, operations, 
# functions, and modifiers to format the value like {age} above.

price = 59
txt = f"The price is {price} dollars"
print(txt)

# A placeholder can include a modifier to format the value.

# A modifier is included by adding a colon : followed by a legal formatting type, 
# like .2f which means fixed point number with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars" # The price is 59.00 dollars
print(txt)

price = 59
txt = f"The price is {price:.4f} dollars" # Display the price with 4 decimals //The price is 59.0000 dollars
print(txt)

name='faruq'
greet='welcome!'

call='{name} {greet} to ibadan'
print(call) #WITHOUT FORMAT //{name} {greet} to ibadan

call=F'{name} {greet} to ibadan'
print(call) # WITH FORMAT //faruq welcome! to ibadan


# A placeholder can contain Python code, like math operations:
age_a = 4
age_b = 10

ages= f'{age_a * age_b}years is 4 x 10 years'
print(ages) # 40years is 4 x 10 years

''' Escape Character

To insert characters that are illegal in a string, use an escape character.
An escape character can be  used to escape any character in a string that is illegal
'''
# txt = "We are the so-called "Vikings" from the north." //ERROR CODE
txt = "We are the so-called \"Vikings\" from the north."
print(txt) #We are the so-called "Vikings" from the north.

# \'	Single Quote	
# \\	Backslash	
# \n	New Line
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value

txt = "We are the so-called \\ from the north."
print(txt) #We are the so-called \ from the north.