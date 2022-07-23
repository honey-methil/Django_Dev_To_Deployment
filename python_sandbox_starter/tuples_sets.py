# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuples use parenthesis

# Create Tuple
fruit_tuple = ('Apple', 'Orange', 'Grape', 'Pear')
# Using Constructor
# fruit_tuple = tuple(('Apple', 'Orange', 'Grape', 'Pear'))

# Get single value by index
print(fruit_tuple[1])

# Cannot change value of tuple or Tuples are unchangeable or immutable
# fruit_tuple[1] = 'Mangoes'

# Tuples with one value should have trailing comma else it will be  a string
fruit_tuple2 = ('Honey',)
fruit_tuple3 = ('Shiva')

# Get length of tuple is ame like list using len function
print(len(fruit_tuple2))

# Delete a tuple
# del fruit_tuple2

print(fruit_tuple)
print(fruit_tuple2)
print(type(fruit_tuple3))


# A Set is a collection which is unordered and unindexed. No duplicate members.
# Sets use curly braces

# Create a set
fruit_set = {'Apples', 'Oranges', 'Strawberries'}

# Ignores duplicates in a set
fruit_set2 = {'Apples', 'Oranges', 'Strawberries', 'Apples'}

# Check if in Set
print('Apple' in fruit_set)
print('Apples' in fruit_set)

print(fruit_set2)
print(fruit_set)

# ----- *************** Changes the Set *********************
# Add to a Set
fruit_set.add('Grapes')

# Remove from a set
fruit_set.remove('Apples')

# Clear a set
fruit_set.clear()

# DELETE a set
# del fruit_set

print(fruit_set)
