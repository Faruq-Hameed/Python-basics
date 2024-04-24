# String variables can be declared either by using single or double quotes:

y= "name"
# Expressions surrounded by backticks are not supported in Python 
# z= `name` //ERROR

# Variable names are case-sensitive.
x= 'john'
X= 'name'
print('x is ', x, '\n', 'X is =', X)

# Variable Names:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

name= 'var-name'
var_name = 'name_name'
_name= 'john'
# Variable names with more than one word can be difficult to read. SO U CAN USE;
MyVar= 'MyVar' # PASCAL CASE NAMING CONVENTION
myVar= 'MyVar' # CAMEL CASE NAMING CONVENTION
My_Var_Name= 'MyVar' # SNAKE CASE NAMING CONVENTION
MyVar2= 'MyVar2' #ALL TH
# name-one= 'John' ERROR CODE

## Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:

names, age, graduate = 'faruq', 12, True

print({names}, {age}, {graduate})

# Note: Make sure the number of variables matches the number of values, or else you will get an error.

# level, married, school = 'five', True// ERROR CODE

# And you can assign the same value to multiple variables in one line:
c = d = f = 'foo'
print({c}, {f}, {d}) # {'foo'} {'foo'} {'foo'}

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. 
# Python allows you to extract the values into variables. This is called unpacking.

fruits = ['apple', 'orange', 'mango']
g,h,i = fruits
print({g}, {h}, {i})

print(g+h+i) # appleorangemango
print(g + h + i) # appleorangemango

# In the print() function, when you try to combine a string 
# and a number with the + operator, Python will give you an error:

# print(g + 8) ERROR: can only concatenate str (not "int") to str
print (g,8)

# Python - Global Variables
# Variables that are created outside of a function (as in all of the examples above) 
# are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

def myFunc():
    print('my fruits are: ' + g, h, i)

myFunc()

# To create a global variable inside a function, you can use the global keyword.
def myFuncA():
    global p
    p = 'pawpaw'
    print('my second fruit is: ', p)

myFuncA()
print({p})

# Also, use the global keyword if you want to change a global variable inside a function.


def myfunc():
  global p
  p = "fantastic"

myfunc()

print("Python is " + p) # //Python is fantastic

x = {"name" : "John", "age" : 36}
print(type(x))

x = True
print(type(x))