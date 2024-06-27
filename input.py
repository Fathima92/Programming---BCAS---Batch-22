favorite_color = input("What's your favorite color? ")
print("Your favorite color is " + favorite_color + ".")


#Task 1
while True:
 try:
    age = int(input("Enter your age: "))
    print("You are " + str(age) + " years old.")
 except ValueError:
    print("Please enter a valid number for age.")
  
# task 2
name = input("Enter your age:     ").strip()

#Task 3
while True:
    user_input = input("Enter a number (or 'q' to quit): ")
    if user_input.lower() == 'q':
        print("Goodbye!")
        break
    try:
        number = int(user_input)
        print("You entered: " + str(number))
    except ValueError:
        print("That's not a valid number. Please try again.")

  #Task 4

    while True:
        try:
            value = int(input("Enter Positive Number"))
            if value > 0:
                print(value)
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input! Please enter a number.")


