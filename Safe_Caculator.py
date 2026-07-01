'''
  Day 11: Exception handling
  Mini-project: Saf calcuator using exception handling
'''
# Exceptions
# Basic syntax
# try:
#     num = int(input('Enter a number: '))
#     result = 10/num
#     print('Result: ', result)
# except ZeroDivisionError:
#     print('Error : Division by zero is not allowed')
# except ValueError:
#     print("Error: Invalid input. Pease enter a valid number")    

# try:
#     # try the code that may raise an exception
# except ExceptionType:
#     # handle the exception
# else:
#     # code to execute if no exception occurs
# finally:
#     # code that will always execute, regardless of whether an exception occurred or not
# # This is the basic syntax of exceptin hndling in python. Now let's look at the exampe in this case
# try:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     result = num1 / num2
#     print("Result: ", result)
# except (ZeroDivisionError, ValueError): # here we are handling two (multiple) exceptions, ZeroDivisionError and ValueError. If any of these exceptions occur, the code inside the except block will be executed.
#     print("Error: Division by zero or invalid input")
# else:
#     print("Calculation completed successfully. No exception occured.")
# finally:
#     print("Thank you for using the safe calculator.")        


# # Custom Exception
# def withdraw(amount):
#     if amount < 0:
#         raise ValueError("Invalid withdrawal amount. Amount cannot be negative.")
#     print(e)



# ----- Mini-project: Safe Calculator -----

# Step 1 Define calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

# Step 2: Display a menu to the user
def show_menu():
    print("\n---- Safe Calculator Menu ----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

# Step 3: Main Program
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Thank you for using the Safe Calculator. Goodbye!")
        break

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == "1":
            result = add(num1, num2)
            print(f"Result: {result}")
        elif choice == "2":
            result = subtract(num1, num2)
            print(f"Result: {result}")
        elif choice == "3":
            result = multiply(num1, num2)
            print(f"Result: {result}")
        elif choice == "4":
            result = divide(num1, num2)
            print(f"Result: {result}")
        else:
            print("Invalid choice. Please select a valid option (1-5).")

    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")  
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Calculation completed. Thank you for using the Safe Calculator.")          