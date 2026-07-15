'''
  Day 22: Bank Account Simulator Using Classes and Objects
  Topics covered:
  1. what are Classes and Objects?
  2. Understanding Class Attributes and Methods
  3. Constructors (__init__ method)
  4. Working with multiple objects
  5. Mini-project: Bank Account Simulator
'''

# What aare classes and objects
'''A class is blueprint for object. It defines attributes,
variables, methods and functions. An object is an instance 
of a class.'''

# # Example
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def display_info(self):
#         print(f"This is a {self.brand} {self.model}.")

# # Create an object
# my_car = Car('Ford', 'Mustang')
# my_car.display_info()

# """
# Attributes are variables that belong to the class or object.
# Methods are the functions that operate on object data.
# """

# # More Examples
# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed

#     def bark(self):
#         print(f'{self.name} is barking!')

# # Create objects (we can make as many objects as we want. This covers working with multiple objects)
# dog1 = Dog("Max", "Golden Retriever")
# dog2 = Dog("Buddy", "Bulldog")

# dog1.bark()
# dog2.bark()

# Constructors(__Init Method)
'''__init__ method is called automatically when an object is created.
It initializes the object attributes'''


# --- Project: Bank Account Simulator ---

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    # funtion for depositing money
    def deposit(self, amount):
        if amount > 0: 
            self.balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            print("Insufficient funds.")

    # Show Account Details
    def show_details(self):
        print("\n--- Account Details ---")
        print(f"Account Holder: {self.account_holder}") 
        print(f"Account Balance: ${self.balance}")

# Main Program
accounts = {}
def create_account():
    name = input("Enter account holder's name: ")
    initial_deposit = float(input("Enter initial deposit amount: "))
    account = BankAccount(name, initial_deposit)
    accounts[name] = account
    print("Account created successfully!")

def access_account():
    name = input('Enter your name: ').strip()
    if name in accounts:
        account = accounts[name]
        while True:
            print("\n--- Menu ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show Details")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            elif choice == "2":
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            elif choice == "3":
                account.show_details()
            elif choice == "4":
                print("Exiting Account menu.")
                break
            else:
                print("Invalid choice. Please select a valid option.")
    else:
        print("Account not found. Please create an account first.")

# Main Menu
while True:
    print("\n--- Bank Account Simulator ---")
    print("1. Create Bank Account.")
    print("2. Access account.")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
       create_account()
    elif choice == '2':
        access_account()
    elif choice == "3":
        print("Exiting Bank Account Simulator.")
        break
    else:
        print("Invalid Choice. Please Enter valid choice")






    