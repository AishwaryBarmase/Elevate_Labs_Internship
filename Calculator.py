def calculator():
    print("Welcome to the Command-Line Calculator!")

    result = None

    while True:

        if result is None:
            try:
                num1 = float(input("Enter the first number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
        else:
            num1 = result

        operation = input("Enter an operation (+, -, *, /) or 'q' to quit: ")

        if operation.lower() == 'q':
            print("Goodbye!")
            break

        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Please enter +, -, *, or /.")
            continue

        try:
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                result = None  # Reset result so the user has to start a new calculation.
                continue
            else:
                result = num1 / num2

        print(f"Result: {result}")
        print(f"You can now perform another operation on the result ({result}) or start a new calculation.")


if __name__ == "__main__":
    calculator()
