name = input("Enter your name: ")
print(f"Hello, {name}!")

age = int(input("Enter your age: "))
print(f"You are {age} years old.")

##############################################################3
height = float(input("Enter your height in meters: "))
print(f"Your height is {height} meters.")

##############################################################
numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
print(f"The numbers are: {numbers}")

##############################################################
is_happy = input("Are you happy? (yes/no): ").strip().lower()
if is_happy == "yes":
    print("That's great to hear!")
else:
    print("I hope things get better soon.")
###########################################################
while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("That's not a valid number. Please try again.")
print(f"You entered the number: {num}")

###################################################################
data = input("Enter some data (or press enter to use default): ") or "default value"
print(f"The data is: {data}")

