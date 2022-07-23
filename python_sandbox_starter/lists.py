# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create List
numbers = [1,2,3,4,5]

# Using Constructors
# numbers = list((1,2,3,4,5))

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']
print(fruits)

print(numbers)
# print(type(numbers))

# Get values by Index
print(fruits[1])

# Get the length of the array
print(len(fruits))

# ----- *************** Changes the list *********************

# Append to the list (value will be appended in the last position)
fruits.append('Mangoes')

# Remove from the list
fruits.remove('Oranges')

# Insert into a specific position
fruits.insert(2, 'Strawberries')

# Delete from a specific position
fruits.pop(1)

# Reverse the list
fruits.reverse()

# Sort the list
fruits.sort()

# Reverse the sort
#fruits.sort(reverse=True)

print(fruits)