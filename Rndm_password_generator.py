'''
  Day 14: Random Password Generator Using Libraries and Modules
  Topcis covered : 
  1. What are Modules adn libraries
  2. Importing libraries
  3. Built-in Python Libraries
  4. Creating and using customs modules
  5. Mini-project: Random password generator
'''
# How to import and use modules and libraries

import math
print(math.sqrt(16))

import random
print(random.randint(1,10))

# We can also import a specific modules from a library
from random import choices
fruits = ["Apple", "Banana", "cherry"]
print(choices(fruits))

# How to use aliases 
import random as rnd
print(rnd.randint(1,5))

# Built-in Python libraries
'''
1. OS
2. Random
3. datetime
4. math
and many more...
'''

# Let's say if want to gnerate a random password

import random

password = ''.join(random.choices('abcdefghijkmnopqrstuvwxyz1234567890', k=8)) # k attribute mean we gie a number there and it will make that number of choces e eneter in the k
print(password)

# Creating and using custom modules
'''
Let's say we make a newe file in the folder named as greetings.py
and in that we make a function that takes name as an input and 
returns a string saying Hello with name we gave input'''

import greetings
print(greetings.say_hello('Muzammil'))
# This is how to make and use our own custom modules 

# ----- Mini-project: Random password generator -----
'''
Generates Password of customizable length,
Which would include Uppercase, Lowercase,
numbers, and special characters. And insure
secure and unique passwords
'''
# Import the important libraries
import random, string

# Step 1: Defining a password generation function
def  generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be atleast 4 characters")
    # Character sets for the password
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine all the character sets
    all_chars = uppercase + lowercase + digits + special_chars
    
    # Ensure at least one of each character type
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill in the remaining length with random choices of all sets
    all_chars = uppercase + lowercase + digits + special_chars
    password += random.choices(all_chars, k=length-4)

    # Shuffle the password to make it more random
    random.shuffle(password)

    # Convert the list into a string and return
    return ''.join(password)

# Step 2: User Interaction
try:
    length = int(input("Enter the desired password length (minimum 4): "))
    password = generate_password(length)
    print("Generated Password: ", password)
except ValueError as e:
    print(e)    

