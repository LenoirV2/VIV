print("Hello World")

user_input = input("Enter a number: ")

try:
    # Convert the user input to an integer
    user_input = int(user_input)

    if user_input >= 0:
        print("Valid input: It's a non-negative number.")
    else:
        print("Invalid input: It's a negative number.")
except ValueError:
    print("Invalid input: It's not a valid number.")
