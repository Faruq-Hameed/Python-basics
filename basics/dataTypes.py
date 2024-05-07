
'''
Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''


# You can convert from one type to another with the int(), float(), and complex()
# e.g 
x= int(5)

print(type(x)) # int

x= float(5) 
print(type(x)) # float
print(x) # 5.0

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

#convert from complex to int: NOT POSSIBLE Error: can't convert complex to int
# You cannot convert complex numbers into another number type.
d= int(z)

print(a) # 1.0
print(b) # 2
print(c) # (1+0j)


print(type(a))
print(type(b))
print(type(c))

# Python has a built-in module called random that can be used to make random numbers:

import random

print(random.randrange(9))