# Creating an empty tuple
empty_tuple = ()
print(empty_tuple)  # Output: ()

# Creating a tuple with integers
numbers = (1, 2, 3, 4, 5)
print(numbers)  # Output: (1, 2, 3, 4, 5)

# Creating a tuple with mixed data types
mixed_tuple = (1, "apple", 3.14, True)
print(mixed_tuple)  # Output: (1, 'apple', 3.14, True)

# Creating a nested tuple
nested_tuple = (1, (2, 3), (4, 5, 6))
print(nested_tuple)  # Output: (1, (2, 3), (4, 5, 6))

# Creating a tuple without parentheses (tuple packing)
packed_tuple = 1, 2, 3, 4, 5
print(packed_tuple)  # Output: (1, 2, 3, 4, 5)

# Accessing elements by index
fruits = ("apple", "banana", "cherry")
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry

# Negative indexing
print(fruits[-1])  # Output: cherry
print(fruits[-2])  # Output: banana

# Accessing nested tuples
nested_tuple = (1, (2, 3), (4, 5, 6))
print(nested_tuple[1])  # Output: (2, 3)
print(nested_tuple[1][1])  # Output: 3

# Unpacking a tuple
numbers = (1, 2, 3)
a, b, c = numbers
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# Unpacking with a different number of variables
fruits = ("apple", "banana", "cherry")
first, *middle, last = fruits
print(first)   # Output: apple
print(middle)  # Output: ['banana']
print(last)    # Output: cherry


# Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)  # Output: (1, 2, 3, 4, 5, 6)

# Repeating tuples
numbers = (1, 2, 3)
result = numbers * 3
print(result)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)


# Using the count() method
numbers = (1, 2, 3, 1, 1, 4)
print(numbers.count(1))  # Output: 3

# Using the index() method
fruits = ("apple", "banana", "cherry")
print(fruits.index("banana"))  # Output: 1

# Checking if an element is in the tuple
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)  # Output: True
print("date" in fruits)    # Output: False

# Finding the length of a tuple
fruits = ("apple", "banana", "cherry")
print(len(fruits))  # Output: 3

# Slicing a tuple
numbers = (1, 2, 3, 4, 5, 6)
print(numbers[1:4])  # Output: (2, 3, 4)
print(numbers[:3])   # Output: (1, 2, 3)
print(numbers[3:])   # Output: (4, 5, 6)
print(numbers[::2])  # Output: (1, 3, 5)

# Creating and accessing nested tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[0])      # Output: (1, 2)
print(nested_tuple[0][1])   # Output: 2
print(nested_tuple[2][0])   # Output: 5
