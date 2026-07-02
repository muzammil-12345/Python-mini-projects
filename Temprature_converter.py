# Day 12: Temperature Converter project
'''
Topics covered:
1. Understanding return values in Functions
2. Using functions to perform Calculations
3. How to return multiple values from a function
4. Best practices for return values
'''
# Simple syntax of a fucntion

def func_name():
    # code block
    return

# Simple fucntion to add two numbers
def add_numbers(num1, num2):
    return num1 + num2  

# calling function
result = add_numbers(10, 20)
print(result)

# Function or finding area of a rectangle
def area_of_rectangle(length, width):
    area = length * width
    return area

# function for math operations
def math_operations(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2
    return addition, subtraction, multiplication, division # This function returns multiple values as a tuple

# calling function
result = math_operations(10, 5)
addition, subtraction, multiplication, division = result
print(f"Addition: {addition}, Subtraction: {subtraction}, Multiplication: {multiplication}, Division: {division}")  


# ----- Mini-project: Temperature Converter -----

# Step 1 : Define a conversion funtionns
def celsius_to_fahrenheit(celsius):
   return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
   return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
   return celsius + 273.15

def kelvin_to_celsius(kelvin):
   return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
   return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
   return (kelvin - 273.15) * 9/5 + 32

# Step 2: Display a menu for the user to choose the conversion type
def show_menu():
    print("\n--- Temperature Converter Menu ---")
    print("1. Celsius to Fahrenheit & Kelvin")
    print("2. Fahrenheit to Celsius & Kelvin")
    print("3. Kelvin to Celsius & Fahrenheit")
    print("4. Exit")

# step 4: Main Program loop

while True:
    show_menu()
    Choice = input("Enter your choice (1-4): ")
    if Choice == "1":
        Celsius = float(input("Enter temperature in Celsius: "))
        print(f"{Celsius}°C = {celsius_to_fahrenheit(Celsius)}°F and {celsius_to_kelvin(Celsius)}K")
    elif Choice == "2":
        Fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{Fahrenheit}°F = {fahrenheit_to_celsius(Fahrenheit)}°C and {fahrenheit_to_kelvin(Fahrenheit)}K")
    elif Choice == "3":
        Kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"{Kelvin}K = {kelvin_to_celsius(Kelvin)}°C and {kelvin_to_fahrenheit(Kelvin)}°F")
    elif Choice == "4":
        print("Exiting the Temperature Converter. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")