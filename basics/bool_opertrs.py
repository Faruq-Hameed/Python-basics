

# The bool() function allows you to evaluate any value, and give you True or False in return,
'''
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.

Example
The following will return True:
'''

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})