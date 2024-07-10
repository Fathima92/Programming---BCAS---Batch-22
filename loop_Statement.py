# List of numbers
numbers = [1, 2, 3, 4, 5]

# For loop to iterate through the list
for number in numbers:
    print(number)

######################################
# Number of levels in the half-pyramid
n = 3
# Outer loop for each level
for i in range(1, n + 1):
    # Inner loop to print stars
    for j in range(i):
        print("*", end="")
    # Move to the next line after each level
    print()
    
######################################
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Variable to store the sum
total_sum = 0

# For loop to iterate through the list and calculate the sum
for number in numbers:
    total_sum += number

print("The sum of the numbers is:", total_sum)

###########################################


# Multiplication table (1 to 5)
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end='\t')
    print()


##########################################


# Dictionary of student grades
grades = {'Alice': 90, 'Bob': 85, 'Charlie': 92}

# For loop to iterate through the dictionary
for student, grade in grades.items():
    print(f"{student}: {grade}")

#########################################
# Number of levels in the pyramid
n = 5

# Outer loop for each level
for i in range(1, n + 1):
    # Print spaces to center the stars
    for j in range(n - i):
        print(" ", end="")
    # Print stars for the current level
    for k in range(2 * i - 1):
        print("*", end="")
    # Move to the next line after each level
    print()
