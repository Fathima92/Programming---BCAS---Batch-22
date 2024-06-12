# Create a list of integers
numbers = [1, 2, 3, 4, 5]
print(numbers)

# Create a list of strings
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Create a mixed list
mixed = [1, "apple", 3.14, True]
print(mixed)

# Accessing elements by index
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry

# Negative indexing
print(fruits[-1])  # Output: cherry
print(fruits[-2])  # Output: banana

# Changing an element
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# Using append() to add an element at the end
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

# Using insert() to add an element at a specific position
fruits.insert(1, "blueberry")
print(fruits)  # Output: ['apple', 'blueberry', 'banana', 'cherry', 'date']


# Using remove() to remove a specific element
fruits = ["apple", "banana", "cherry", "date"]
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry', 'date']

# Using pop() to remove an element by index
fruits.pop(1)
print(fruits)  # Output: ['apple', 'date']

# Using del to remove an element by index
del fruits[0]
print(fruits)  # Output: ['date']

# Sorting a list in ascending order
numbers = [5, 3, 1, 4, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4, 5]

# Sorting a list in descending order
numbers.sort(reverse=True)
print(numbers)  # Output: [5, 4, 3, 2, 1]

# Using sorted() to sort without modifying the original list
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 3, 4, 5]
print(numbers)         # Output: [5, 4, 3, 2, 1]

# Finding the length of a list
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # Output: 3

# Checking if an element is in the list
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # Output: True
print("date" in fruits)    # Output: False
