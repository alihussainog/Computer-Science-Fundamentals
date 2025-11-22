# Function for addition
def add(x, y):
    return x + y

# Function for substraction
def subtract(x, y):
    return x - y

# Function for multiplicaton
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    # Division by zero
    if y == 0:
        return "Error! Cannot divide by zero."
    return x / y

# Calculator Programming
def calculator():
    print("Python Calculator")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    while True:
        # Take input from the user
        choice = input("\nEnter choice (1/2/3/4) or 'q' to quit: ")

        # Check if user wants to quit
        if choice.lower() == 'q':
            print("Thank you for using the calculator. Goodbye!")
            break

        # Check if choice is one of the four operations
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            result = None
            if choice == '1':
                result = add(num1, num2)
                print(f"\n{num1} + {num2} = {result}")

            elif choice == '2':
                result = subtract(num1, num2)
                print(f"\n{num1} - {num2} = {result}")

            elif choice == '3':
                result = multiply(num1, num2)
                print(f"\n{num1} * {num2} = {result}")

            elif choice == '4':
                result = divide(num1, num2)
                # Check for the division by zero error message
                if isinstance(result, str):
                    print(f"\n{result}")
                else:
                    print(f"\n{num1} / {num2} = {result}")
        else:
            print("Invalid input. Please enter a valid choice.")

# Execute the main function when the script is run
if __name__ == "__main__":
    calculator()
