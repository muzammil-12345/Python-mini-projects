'''
 Day 26: Secure Usr profile app Using Encapsulation
 Topic Covered:
 1. What is Encapsulation
 2. Public, Protected, and Private Attributes
 3. Getter and Setter Methods
 4. Validating User data
 5. Project: Secure User Profile App
'''

# What is Encapsulation?
'''
Encapsulation is the practie of restricting direct
access to an object's data and allowing controlled
access through methods. It protects sensitive data
from unintended changes, it ensures data integrity
and validation, and also promotes modularity and
security. 
'''

# # Example
# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

#     def get_password(self):
#         return "*****"

#     def set_password(self, new_password):
#         if len(new_password) >= 8:
#             self.__password = new_password
#             print("Password Updated Successfully!")
#         else:
#             print("Password must be atleast 8 characters")

# user = User("Muzammil_zulfiqar", "Secure123")
# print(user.username)
# print(user.get_password())
# user.set_password("New password")

# # Public, protected and private attributes
# class UserProfile:
#     def __init__(self, username, email, password):
#         self.username = username        # public
#         self.email = email              # public
#         self.__password = password      # private

#     def show_profile(self):
#         print(f"Username: {self.username} ")   # public, accessible anywhere
#         print(f"Email: {self.email}")           # public, accessible anywhere
#         print(f"Password: {self.__password}")   # private, only accessible inside class

# user = UserProfile("Muzammil", "abc@example.com", "Secure123")
# user.show_profile()

# # Getter and Setter methods

# class Account:
#     def __init__(self, balance):
#         self.__balance = balance    # private attribute

#     def get_balance(self):
#         return self.__balance       # getter, value return karta hai

#     def set_balance(self, new_balance):
#         if new_balance >= 0:                    # validation check
#             self.__balance = new_balance
#             print("Balance Updated Successfully")
#         else:
#             print("Invalid Account balance")

# account = Account(1000)
# print(account.get_balance())    # getter call

# account.set_balance(1500)       # setter call, valid value
# print(account.get_balance())

# # Validating User Data

# class User:
#     def __init__(self, username):
#         self.username = username
#         self.__password = None      # private, initially empty

#     def set_password(self, password):
#         if len(password) < 6:                              # validation check
#             print("Password must be atleast 6 characters long")
#         else:
#             self.__password = password
#             print("Password set successfully")

#     def get_password(self):
#         return self.__password      # getter

# user = User("Muzammil")
# user.set_password("secure123")   # 8 characters, valid
# print(user.get_password())

# --- Project: Secure Profile App ---
'''
1. Manages User profiles with secure passwords
2. Validates password strength
3. Provides controlled access to users data
'''

class UserProfile:
    def __init__(self, username, email, password):
        self.username = username         # public
        self._email = email              # protected
        self.__password = password       # private
        self.set_password(password)      # set with validation

    def get_email(self):                 # getter for email
        return self._email

    def set_email(self, new_email):      # setter for email, with validation
        if "@" in new_email and "." in new_email:
            self._email = new_email
            print("Email updated successfully!")
        else:
            print("Invalid email format.")

    def set_password(self, new_password):   # setter for password, with validation
        if len(new_password) < 6:
            print("Password must be atleast 6 characters.")
        else:
            self.__password = new_password
            print("Password set successfully")

    def display_profile(self):           # prints the profile
        print("\n --- User Profile ---")
        print(f"Username: {self.username} ")
        print(f"Email: {self._email} ")
        print(f"Password: {self.__password} ")


# Main program
users = []

def create_user():
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    user = UserProfile(username, email, password)
    users.append(user)
    print("User created successfully.")

def view_profiles():
    if not users:
        print("No users found")
    else:
        for user in users:
            user.display_profile()

def update_email():
    username = input("Enter username to update: ")
    found = False
    for user in users:
        if user.username == username:
            new_email = input("Enter new email: ")
            user.set_email(new_email)
            found = True
            break                     # stop the loop once matched

    if not found:                     # check only after the loop ends
        print("User not found!")


# Main Menu
while True:
    print("\n --- Secure User Profile ---")
    print("1. Create User")
    print("2. View all Profiles")
    print("3. Update Email")
    print("4. Exit")

    choice = input("Enter your Choice: ")
    if choice == "1":
        create_user()
    elif choice == "2":
        view_profiles()
    elif choice == "3":
        update_email()
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid Input. Please enter (1-4).")