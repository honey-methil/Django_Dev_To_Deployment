# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

x = 3                   # Integer. Can be positive or negative
y = 11.5                # Float or decimal. Can be positive or negative
firstName = "Honey"     # String or alpha text
isCool = True           # Bool

print(x, y, firstName, isCool)      # Multiple Print

# Multiple assignment
a, b, lastName, isHot = (22, 31.6, "Methil", False)

print(a, b, lastName, isHot)

# Basic Math
z = a + b
print(z)

# Data Type
print(type(a))
print(type(b))
print(type(lastName))
print(type(isHot))

# Casting
a = float(a)
b = int(b)
z = str(z)

print((a,b,z))
print(type(a), type(b), type(z))


