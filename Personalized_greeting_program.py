# Day 2: Variables, Data Types, and Personalized Greeting Program

# Storing a name in a variable
name = "Muzammil"
nameOfPerson = "Zulfiqars"

# Storing an age in a variable
age = 19

# String
name = "Muzammil"

# Integer
age = 19

# Float
height = 5.6

# Boolean
is_student = False

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

age = "19"

myAge = int(age)

print(myAge + 5)

name = "Muzammil"

print("Hello, " + name + "!")

print("Hello My Friend, {}!".format(name))

print(f"Hello, {name}!")

# Personalized Greeting Program

# Step 1: Ask for user details
name = input("What is your name? ")
age = int(input("How old are you? "))
color = input("What is your favorite color? ")

# Step 2: Generate a personalized greeting message
print("\n---- Personalized Greeting ----")
print(f"Hello, {name}! ")
print(f"You are {age} years old and {color} is a beautiful color!")
print("You're now ready to start your Python adventure.")