# Strings in python are surrounded by either single or double quotation marks.
# Let's look at string formatting and some string methods

name = "Honey"
age = 51

# Concatenate
print("Hello, I am " + name + " and I am " + str(age))

# String Formatting

# Arguments by position
print("{}, {}, {}".format("car", "bus", "jeep"))  # if arguments not mentioned it takes 0, 1, 2, ...
print("{1}, {2}, {0}".format("mouse", "keyboard", "cpu"))
print("{0}, {1}, {2}".format("mouse", "keyboard", "cpu"))

# Arguments by name
print("Hello {pname}, {page} is the new 31".format(pname=name, page=age))

# F-Strings (only in 3.6+)
print(f"Hello {name}, {age} is the new 31")

# String Methods

s = "hello There world"

""" --- Alter the string ---"""
# Capitalize the first letter. Does not change the original
print(s.capitalize())

# All letters in upper. Does not change the original
print(s.upper())

# All letters in lower. Does not change the original
print(s.lower())

# Swap case. Does not change the original
print(s.swapcase())

# Replace. Does not change the original
print(s.replace("world", "everyone"))

""" --- End alter ---"""

""" --- Check for something ---"""
# Starts with a letter or word. Returns boolean. Does not change the original
print(s.startswith("hello"))
print(s.startswith("he"))

# Ends with a letter or word. Returns boolean. Does not change the original
print(s.endswith("world"))

# Is all alphanumeric. No spaces else False
print(s.isalnum())

# Is all alphabetic. No spaces and No numeric else False
print(s.isalpha())

# Is all numeric. No spaces and No alpha else False
print(s.isnumeric())

# Check for all .is methods available

""" --- End Check ----------"""

""" --- Number Count something ---"""
# Count a letter or word within a string. Does not change the original
print(s.count("e"))

# Get Length. Does not change the original
print(len(s))

""" --- End Count ----------"""

# Split into a list
print(s.split())

# Find position
print(s.find("r"))



print(s)

